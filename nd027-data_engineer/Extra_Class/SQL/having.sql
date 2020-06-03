# having should be after group by (aggregation), and before order by
# where appears after from, join, and on, but before group by

--How many of the sales reps have more than 5 accounts that they manage?
select s.name, count(*) from sales_reps s inner join accounts a on a.
sales_rep_id = s.id group by s.name having count(*) > 5

--How many accounts have more than 20 orders?
select a.name, count(*) from accounts a inner join orders o on o.account_id=a.id 
group by a.name having count(*) > 20

Which account has the most orders?
select a.name, count(*) from accounts a inner join orders o on o.account_id=a.id 
group by a.name order by count(*) limit 1

Which accounts spent more than 30,000 usd total across all orders?
select account_id, sum(total_amt_usd) from orders group by account_id having sum(
total_amt_usd) > 30000

Which accounts spent less than 1,000 usd total across all orders?


Which account has spent the most with us?


Which account has spent the least with us?


Which accounts used facebook as a channel to contact customers more than 6 times?
select a.id, w.channel, count(*) from accounts a inner join web_events w 
on a.id=w.account_id where channel = 'facebook' group by 1, 2 having count(*) > 6

Which account used facebook most as a channel?
select a.id, w.channel, count(*) from accounts a inner join web_events w 
on a.id=w.account_id where channel = 'facebook' group by 1, 2 order by count(*) desc 
limit 1

Which channel was most frequently used by most accounts?
select channel, count(account_id) from web_events group by channel order by count(
account_id) desc limit 1


