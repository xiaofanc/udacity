
-- find the web events occurred before the order
example:
select o.id, o.occurred_at, w.*
from orders o left join web_events w
on w.account_id = o.account_id
and w.occured_at < o.occurred_at
where DATA_TRUNC('month', o.occurred_at) = 
(select DATA_TRUNC('month', min(o.occurred_at)) from orders)
order by o.occurred_at, o.occurred_at

-- In the following SQL Explorer, write a query that left joins the accounts table and the sales_reps tables on each sale rep's ID number and joins it using the < comparison operator on accounts.primary_poc < sales_reps.name

select a.name, a.primary_poc, s.name as s_name from accounts a
left join sales_reps s on a.sales_rep_id = s.id
where a.primary_poc < s.name

-- self join:
-- find the orders within 30 days for each account
select o1.id as o1_id,
       o1.account_id as o1_account,
       o1.occurred_at as o1_occurred,
       o2.id as o2_id,
       o2.account_id as o2_account,
       o2.occurred_at as o2_occurred
from orders o1 
left join orders o2 
on o1.account_id = o2.account_id
and o2.occurred_at > o1.occurred_at
and o2.occurred_at <= o1.occurred_at + INTERVAL '28 days'
order by o1.occurred_at, o2.occurred_at


select w1.id as w1_id,
       w1.account_id as w1_account,
       w1.occurred_at as w1_occurred,
       w1.channel as w1_cha,
       w2.id as w2_id,
       w2.account_id as w2_account,
       w2.occurred_at as w2_occurred,
       w2.channel as w2_cha
from web_events w1 
left join web_events w2 
on w1.account_id = w2.account_id
and w2.occurred_at > w1.occurred_at
and w2.occurred_at <= w1.occurred_at + INTERVAL '1 day'
order by w1.occurred_at, w2.occurred_at

----------------------------------------------------------------
create table web (id varchar, aid varchar);

insert into web (id, aid) values 
('w1', 'a1'),
('w2', 'a1'),
('w3', 'a1'),
('w4', 'a2'),
('w5', 'a2');

select w1.id, w2.id from web w1 left join web w2 on w1.aid = w2.aid;
 id | id 
----+----
 w1 | w3
 w1 | w2
 w1 | w1
 w2 | w3
 w2 | w2
 w2 | w1
 w3 | w3
 w3 | w2
 w3 | w1
 w4 | w5
 w4 | w4
 w5 | w5
 w5 | w4
(13 rows)




