--Which account (by name) placed the earliest order? Your solution should have the account name and the date of the order.

select a.name, o.occurred_at as min_val from orders o inner join accounts a on o.account_id = a.id order by min_val limit 1;

--Find the total sales in usd for each account. You should include two columns - the total sales for each company's orders in usd and the company name.

select sum(o.total_amt_usd), a.name from orders o inner join accounts a on o.account_id=a.id group by a.name

--Via what channel did the most recent (latest) web_event occur, which account was associated with this web_event? Your query should return only three values - the date, channel, and account name.

select channel, occurred_at, name from web_events w inner join accounts a on a.id = w.account_id where occurred_at = (select max(occurred_at) from web_events) 

select w.occurred_at, w.channel, a.name from (
select * from web_events where occurred_at = (
select max(occurred_at) from web_events)) w inner join accounts a 
on a.id=w.account_id

--Find the total number of times each type of channel from the web_events was used. Your final table should have two columns - the channel and the number of times the channel was used.

select channel, count(*) from web_events group by channel

--Who was the primary contact associated with the earliest web_event?

select a.primary_poc from (
select * from web_events where occurred_at = (
select min(occurred_at) from web_events)) w inner join accounts a 
on a.id=w.account_id

--What was the smallest order placed by each account in terms of total usd. Provide only two columns - the account name and the total usd. Order from smallest dollar amounts to largest.

select a.name, sum(o.total_amt_usd) as total from accounts a inner join orders o on a.id = o.account_id group by a.name order by total 

--Find the number of sales reps in each region. Your final table should have two columns - the region and the number of sales_reps. Order from fewest reps to most reps.

select r.name, count(s.id) from region as r inner join sales_reps s on s.region_id = r.id group by 1 order by 2


--Have any sales reps worked on more than one account?
select sale_name from (
select s.name as sale_name, count(a.*) as cnt from sales_reps s inner join accounts a on a.sales_rep_id = s.id group by s.name ) c where cnt > 1;
