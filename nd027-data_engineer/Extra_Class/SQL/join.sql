--1.Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.

select r.name as r_name, s.name as s_name, a.name as a_name 
from sales_reps as s inner join accounts as a on a.sales_rep_id = s.id 
inner join region as r on r.id = s.region_id and r.name = 'Midwest' 
order by a.name

--2.Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for accounts where the sales rep has a first name starting with S and in the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.

select r.name as r_name, s.name as s_name, a.name as a_name 
from sales_reps as s 
inner join accounts as a on a.sales_rep_id = s.id 
inner join region as r on r.id = s.region_id and s.name like 'S%' and r.name = 'Midwest' 
order by a.name

--3. Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for accounts where the sales rep has a last name starting with K and in the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.

select r.name as r_name, s.name as s_name, a.name as a_name 
from sales_reps as s 
inner join accounts as a on a.sales_rep_id = s.id 
inner join region as r on r.id = s.region_id and s.name like '% K%' and r.name = 'Midwest' 
order by a.name

--4. Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order. However, you should only provide the results if the standard order quantity exceeds 100. Your final table should have 3 columns: region name, account name, and unit price. In order to avoid a division by zero error, adding .01 to the denominator here is helpful total_amt_usd/(total+0.01).

select r.name as r_name, o.total_amt_usd/(o.total+0.01) as unit_price, a.name as a_name 
from sales_reps as s 
inner join accounts as a on a.sales_rep_id = s.id 
inner join region as r on r.id = s.region_id 
inner join orders as o on o.account_id = a.id and o.standard_qty > 100
order by a.name

--5. Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order. However, you should only provide the results if the standard order quantity exceeds 100 and the poster order quantity exceeds 50. Your final table should have 3 columns: region name, account name, and unit price. In order to avoid a division by zero error, adding .01 to the denominator here is helpful (total_amt_usd/(total+0.01).

select r.name as r_name, o.total_amt_usd/(o.total+0.01) as unit_price, a.name as a_name 
from sales_reps as s 
inner join accounts as a on a.sales_rep_id = s.id 
inner join region as r on r.id = s.region_id 
inner join orders as o on o.account_id = a.id and o.poster_qty > 50 and o.standard_qty > 100
order by a.name

--6. Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order. However, you should only provide the results if the standard order quantity exceeds 100 and the poster order quantity exceeds 50. Your final table should have 3 columns: region name, account name, and unit price. Sort for the largest unit price first. In order to avoid a division by zero error, adding .01 to the denominator here is helpful (total_amt_usd/(total+0.01).

select r.name as r_name, o.total_amt_usd/(o.total+0.01) as unit_price, a.name as a_name 
from sales_reps as s 
inner join accounts as a on a.sales_rep_id = s.id 
inner join region as r on r.id = s.region_id 
inner join orders as o on o.account_id = a.id and o.poster_qty > 50 and o.standard_qty > 100
order by unit_price desc

--7.What are the different channels used by account id 1001? Your final table should have only 2 columns: account name and the different channels. You can try SELECT DISTINCT to narrow down the results to only the unique values.

select DISTINCT a.name, w.channel from accounts a inner join web_events w on a.id = w.account_id and a.id =
'1001'

--8. Find all the orders that occurred in 2015. Your final table should have 4 columns: occurred_at, account name, order total, and order total_amt_usd.

select o.occurred_at, a.name as a_name, o.total, o.total_amt_usd from accounts as a inner join orders as 
o on o.account_id = a.id and o.occurred_at between '2015-01-01' and '2016-01-01'


