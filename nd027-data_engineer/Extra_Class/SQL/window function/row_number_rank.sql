

# display the row number 
select id,
    account_id,
    occurred_at,
    ROW_NUMBER() over (order by occurred_at) as row_num
from orders

# display the row number within each partition
select id,
    account_id,
    occurred_at,
    ROW_NUMBER() over (partition by account_id order by occurred_at) as row_num
from orders

# for same occurred_at:
# rank() gives same rank and skip values
# while row_number gives different numbers
# dense_rank() does not skip values

select id,
    account_id,
    occurred_at,
    RANK() over (partition by account_id order by occurred_at) as row_num
from orders

select id,
    account_id,
    occurred_at,
    DATE_TRUNC('month', occurred_at) as month,
    RANK() over (partition by account_id order by DATE_TRUNC('month', occurred_at)) as row_num
from orders  

select id,
    account_id,
    occurred_at,
    DATE_TRUNC('month', occurred_at) as month,
    DENSE_RANK() over (partition by account_id order by DATE_TRUNC('month', occurred_at)) as row_num
from orders


value  row_number()   rank()   dense_rank()
10        1             1           1
11        2             2           2
11        3             2           2
13        4             4           3
13        5             4           3
15        6             6           4

-- Ranking Total Paper Ordered by Account
-- Select the id, account_id, and total variable from the orders table, then create a column called total_rank that ranks this total amount of paper ordered (from highest to lowest) for each account using a partition. Your final table should have these four columns.

select id, 
    account_id,
    total, 
    rank() over (partition by account_id order by total desc) as rank 
from orders

-- Aggregates in Window Functions with and without ORDER BY
SELECT id,
       account_id,
       standard_qty,
       DATE_TRUNC('month', occurred_at) AS month,
       DENSE_RANK() OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS dense_rank,
       SUM(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS sum_std_qty,
       COUNT(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS count_std_qty,
       AVG(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS avg_std_qty,
       MIN(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS min_std_qty,
       MAX(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS max_std_qty
FROM orders

# total is not the running toal without order by
# dense_rank is constant at 1 for all rows for all account_id
# row_number() works
# leaving the ORDER BY out is equivalent to "ordering" in a way that all rows in the partition are "equal" to each other. 

SELECT id,
       account_id,
       standard_qty,
       DATE_TRUNC('month', occurred_at) AS month,
       DENSE_RANK() OVER (PARTITION BY account_id) AS dense_rank,
       SUM(standard_qty) OVER (PARTITION BY account_id) AS sum_std_qty,
       COUNT(standard_qty) OVER (PARTITION BY account_id) AS count_std_qty,
       AVG(standard_qty) OVER (PARTITION BY account_id) AS avg_std_qty,
       MIN(standard_qty) OVER (PARTITION BY account_id) AS min_std_qty,
       MAX(standard_qty) OVER (PARTITION BY account_id) AS max_std_qty
FROM orders

# alias for window
SELECT id,
       account_id,
       standard_qty,
       DATE_TRUNC('month', occurred_at) AS month,
       DENSE_RANK() OVER main_window AS dense_rank,
       SUM(standard_qty) OVER main_window AS sum_std_qty,
       COUNT(standard_qty) OVER main_window AS count_std_qty,
       AVG(standard_qty) OVER main_window AS avg_std_qty,
       MIN(standard_qty) OVER main_window AS min_std_qty,
       MAX(standard_qty) OVER main_window AS max_std_qty
FROM orders

WINDOW main_window as (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at))



