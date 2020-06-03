-- day/month/year/second
2011-01-03 12:30:00
DATE_TRUNC: 'day': 2011-05-03 'month': 2011-05-01 'year': 2011-01-01
DATE_PART:  'day': 03 'month': 05 'year': 2011

select DATE_TRUNC('day', occurred_at) as day,
    sum(standard_qty) as total_qty
    from orders
    group by DATE_TRUNC('day', occurred_at)
    order by DATE_TRUNC('day', occurred_at)

select DATE_PART('dow', occurred_at) as day, # day of week
    sum(standard_qty) as total_qty
    from orders
    group by DATE_TRUNC('day', occurred_at)
    order by DATE_TRUNC('day', occurred_at)

--Find the sales in terms of total dollars for all orders in each year, ordered from greatest to least. Do you notice any trends in the yearly sales totals?
select DATE_PART('year', occurred_at) as yr, sum(total_amt_usd) as total from orders 
group by 1 order by 2 desc 

--Which month did Parch & Posey have the greatest sales in terms of total dollars? Are all months evenly represented by the dataset?
select DATE_PART('month', occurred_at) as yr, sum(total_amt_usd) as total from 
orders group by 1 order by 2 desc 

--Which year did Parch & Posey have the greatest sales in terms of total number of orders? Are all years evenly represented by the dataset?
select DATE_PART('year', occurred_at) as yr, count(*) as total from orders 
group by 1 order by 2 desc 

--Which month did Parch & Posey have the greatest sales in terms of total number of orders? Are all months evenly represented by the dataset?
select DATE_PART('month', occurred_at) as yr, count(*) as total from orders 
group by 1 order by 2 desc 

--In which month of which year did Walmart spend the most on gloss paper in terms of dollars?
select DATE_TRUNC('month', occurred_at) as yr,  sum(gloss_amt_usd) as total from 
orders o inner join accounts a on a.id = o.account_id where a.name ='Walmart' group 
by 1 order by 2 desc 
