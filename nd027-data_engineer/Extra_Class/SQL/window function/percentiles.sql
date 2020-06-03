
# NTILE 分组, which group standard_qty falls for 
select id,
    account_id,
    occurred_at,
    standard_qty,
    NTILE(4) OVER (ORDER BY standard_qty) as quartile,
    NTILE(5) OVER (ORDER BY standard_qty) as quintile,
    NTILE(100) OVER (ORDER BY standard_qty) as percentile,
from orders
order by standard_qty desc

# window alias
select id,
    account_id,
    occurred_at,
    standard_qty,
    NTILE(4) OVER mainwindow as quartile,
    NTILE(5) OVER mainwindow as quintile,
    NTILE(100) OVER mainwindow as percentile
from orders
WINDOW mainwindow as (ORDER BY standard_qty)
order by standard_qty desc


# divide orders into several levels for each account_id!

--Use the NTILE functionality to divide the account into 4 levels in terms of the amount of standard_qty for their orders. Your resulting table should have the account_id, the occurred_at time for each order, the total amount of standard_qty paper purchased, and one of four levels in a standard_quartile column.
select 
    account_id,
    occurred_at,
    standard_qty,
    NTILE(4) OVER mainwindow as quartile
from orders
WINDOW mainwindow as (PARTITION BY account_id ORDER BY standard_qty)
order by account_id desc


--Use the NTILE functionality to divide the accounts into two levels in terms of the amount of gloss_qty for their orders. Your resulting table should have the account_id, the occurred_at time for each order, the total amount of gloss_qty paper purchased, and one of two levels in a gloss_half column.
select 
    account_id,
    occurred_at,
    gloss_qty,
    NTILE(2) OVER mainwindow as levels
from orders
WINDOW mainwindow as (PARTITION BY account_id ORDER BY gloss_qty)
order by account_id desc

--Use the NTILE functionality to divide the orders for each account into 100 levels in terms of the amount of total_amt_usd for their orders. Your resulting table should have the account_id, the occurred_at time for each order, the total amount of total_amt_usd paper purchased, and one of 100 levels in a total_percentile column.
SELECT
   account_id,
   occurred_at,
   total_amt_usd,
   NTILE(100) OVER (PARTITION BY account_id ORDER BY total_amt_usd) AS total_percentile
  FROM orders 
 ORDER BY account_id DESC

