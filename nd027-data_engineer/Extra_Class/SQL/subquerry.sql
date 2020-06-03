select channel, avg(total) from 
(select channel, DATE_TRUNC('day', occurred_at) as day, count(*) as total from web_events group by 1, 2 order by 3 desc) a 
group by 1 order by 2 desc

select *
from orders
where DATE_TRUNC('day', occurred_at) = 
(select DATE_TRUNC('day', min(occurred_at)) as min_month
from orders)
order by occurred_at

select avg(standard_qty) as s, avg(gloss_qty) as g, avg(poster_qty) as p
from orders where DATE_TRUNC('month', occurred_at) =  
(select DATE_TRUNC('month', min(occurred_at)) as min_month from orders) 

--Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.

# t1 - get the sum of total_amt_usd for each rep in each region
# t2 - find the largest amount of total_amt_usd sales for each region first
# t3 - join with t3 on region and total amount to find the reps name

select t3.name, t3.region, t3.total from
    (select region, max(total) as total from 
        (select s.name as name, r.name as region, sum(o.total_amt_usd) as total 
        from region r 
        inner join sales_reps s on r.id = s.region_id 
        inner join accounts a on s.id =a.sales_rep_id 
        inner join orders o on o.account_id = a.id group by 1,2) t1
        group by 1) t2
    join 
    (select s.name as name, r.name as region, sum(o.total_amt_usd) as total 
    from region r 
    inner join sales_reps s on r.id = s.region_id 
    inner join accounts a on s.id =a.sales_rep_id 
    inner join orders o on o.account_id = a.id group by 1,2) t3
    on t3.region = t2.region and t3.total = t2.total;


--For the region with the largest (sum) of sales total_amt_usd, how many total (count) orders were placed?

# t1 - get the sum of amount for each region
# t2 - get the max of total for all regions
# t3 - join with t3 on total to get the orders count

select t3.region, t3.total_orders from (
    select max(total) as total from (
        select r.name as region, 
        sum(o.total_amt_usd) as total 
        from region r 
        inner join sales_reps s on r.id = s.region_id 
        inner join accounts a on s.id =a.sales_rep_id 
        inner join orders o on o.account_id = a.id 
        group by 1) t1
) t2

join (
    select r.name as region, 
    sum(o.total_amt_usd) as total, 
    count(o.id) as total_orders 
    from region r 
    inner join sales_reps s on r.id = s.region_id 
    inner join accounts a on s.id =a.sales_rep_id 
    inner join orders o on o.account_id = a.id 
    group by 1) t3
on t2.total = t3.total

--How many accounts had more total purchases than the account name which has bought the most standard_qty paper throughout their lifetime as a customer?

# t1 -find the total purchase of the account which has bought the most stadard_qty paper 
# get the accounts which had more total purchases using having
# count finally

select count(*) from (
    select a.name, sum(o.total)
    from accounts a join orders o on o.account_id = a.id
    group by 1
    having sum(o.total) > (
        select total from (
            select a.name as name,
            sum(o.standard_qty) as total_s,
            sum(o.total) as total 
            from accounts a join orders o on a.id = o.account_id
            group by 1
            order by 2 desc 
            limit 1
        ) t1
    )
) t2;

--For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?

select channel, count(*) as events 
from web_events 
where account_id = (
    select account_id from (
        select account_id, 
        sum(total_amt_usd) 
        from orders 
        group by 1
        order by 2 desc
        limit 1 ) t1 )
group by 1

--What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?

select avg(total) from (
    select account_id, 
    sum(total_amt_usd) as total 
    from orders 
    group by 1
    order by 2 desc
    limit 10) t


--What is the lifetime average amount spent in terms of total_amt_usd, including only the companies that spent more per order, on average, than the average of all orders.

select avg(a) from (
    select account_id, avg(total_amt_usd) as a 
    from orders 
    group by 1 
    having avg(total_amt_usd) > (
        select avg(total_amt_usd) from orders
    ) 
) t




