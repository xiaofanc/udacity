# also called common table expression

with events as (select channel, 
    DATE_TRUNC('day', occurred_at) as day, 
    count(*) as total 
    from web_events 
    group by 1, 2 
    order by 3 desc)

select channel, avg(total) 
from events 
group by 1 
order by 2 desc

WITH table1 AS (
          SELECT *
          FROM web_events),

     table2 AS (
          SELECT *
          FROM accounts)

SELECT *
FROM table1
JOIN table2
ON table1.account_id = table2.id;

--Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.

# t1 - get the sum of total_amt_usd for each rep in each region
# t2 - find the largest amount of total_amt_usd sales for each region first
# t3 - join with t3 on region and total amount to find the reps name

with t1 as (select s.name as name, r.name as region, sum(o.total_amt_usd) as total 
        from region r 
        inner join sales_reps s on r.id = s.region_id 
        inner join accounts a on s.id =a.sales_rep_id 
        inner join orders o on o.account_id = a.id group by 1,2),

     t2 as (select region, max(total) as total from t1
        group by 1)

select t1.name, t1.region, t1.total from t2 join t1
    on t1.region = t2.region and t1.total = t2.total;


--For the region with the largest (sum) of sales total_amt_usd, how many total (count) orders were placed?

# t1 - get the sum of amount for each region
# t2 - get the max of total for all regions
# t3 - join with t3 on total to get the orders count

with t1 as (select r.name as region, 
        sum(o.total_amt_usd) as total,
        count(o.id) as total_orders 
        from region r 
        inner join sales_reps s on r.id = s.region_id 
        inner join accounts a on s.id =a.sales_rep_id 
        inner join orders o on o.account_id = a.id 
        group by 1),
    
    t2 as (select max(total) as total from t1)
    
select t1.region, t1.total_orders from t2 join t1
on t2.total = t1.total

--How many accounts had more total purchases than the account name which has bought the most standard_qty paper throughout their lifetime as a customer?

# t1 -find the total purchase of the account which has bought the most stadard_qty paper 
# get the accounts which had more total purchases using having
# count finally

with t1 as (select a.name as name,
            sum(o.standard_qty) as total_s,
            sum(o.total) as total 
            from accounts a join orders o on a.id = o.account_id
            group by 1
            order by 2 desc 
            limit 1)


select count(*) from (
    select a.name, sum(o.total)
    from accounts a join orders o on o.account_id = a.id
    group by 1
    having sum(o.total) > (
        select total from t1
    )
) t2;

--For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?

with t1 as (select account_id, 
        sum(total_amt_usd) 
        from orders 
        group by 1
        order by 2 desc
        limit 1)

select channel, count(*) as events 
from web_events 
where account_id = (
    select account_id from t1 )
group by 1

--What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?

with t as (select account_id, 
    sum(total_amt_usd) as total 
    from orders 
    group by 1
    order by 2 desc
    limit 10)

select avg(total) from t


--What is the lifetime average amount spent in terms of total_amt_usd, including only the companies that spent more per order, on average, than the average of all orders.

with t as (select account_id, avg(total_amt_usd) as a 
    from orders 
    group by 1 
    having avg(total_amt_usd) > (
        select avg(total_amt_usd) from orders
    ) )

select avg(a) from t