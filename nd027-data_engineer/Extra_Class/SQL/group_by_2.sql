--For each account, determine the average amount of each type of paper they purchased across their orders. Your result should have four columns - one for the account name and one for the average quantity purchased for each of the paper types for each account.

select a.name, avg(o.standard_qty) as mean_s, avg(o.gloss_qty) as mean_g, avg(o.
poster_qty) as mean_p from accounts a inner join orders o on o.account_id = a.id 
group by a.name;

--For each account, determine the average amount spent per order on each paper type. Your result should have four columns - one for the account name and one for the average amount spent on each paper type.

select a.name, avg(o.standard_amt_usd) as mean_s, avg(o.gloss_amt_usd) as mean_g, avg
(o.poster_amt_usd) as mean_p from accounts a inner join orders o on o.account_id = a.
id group by a.name;

--Determine the number of times a particular channel was used in the web_events table for each sales rep. Your final table should have three columns - the name of the sales rep, the channel, and the number of occurrences. Order your table with the highest number of occurrences first.

SELECT s.name, w.channel, COUNT(*) num_events
FROM accounts a
JOIN web_events w
ON a.id = w.account_id
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY s.name, w.channel
ORDER BY num_events DESC;

--Determine the number of times a particular channel was used in the web_events table for each region. Your final table should have three columns - the region name, the channel, and the number of occurrences. Order your table with the highest number of occurrences first.

SELECT r.name, w.channel, COUNT(*) num_events
FROM accounts a
JOIN web_events w
ON a.id = w.account_id
JOIN sales_reps s
ON s.id = a.sales_rep_id
JOIN region r
on r.id = s.region_id
GROUP BY r.name, w.channel
ORDER BY num_events DESC;

