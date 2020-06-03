
# running total order by occurred_at
# standard_qty   running_total
#     0               0
#     2               2
#     3               5
#     9               14

select standard_qty,
    sum(standard_qty) over (order by occurred_at) as running_total
from orders

# running total by month order by occurred_at
# without order by, the total will be the same for each month
select standard_qty,
    DATE_TRUNC('month', occurred_at) as month,
    sum(standard_qty) over (partition by DATE_TRUNC('month', occurred_at) order by occurred_at) as running_total
from orders

select standard_amt_usd, occurred_at, date_part('year', occurred_at) as yr, 
    sum(standard_amt_usd) over(partition by 3 order by occurred_at)
from orders

select standard_amt_usd, occurred_at, date_part('year', occurred_at) as yr, 
    sum(standard_amt_usd) over(partition by 3 order by occurred_at)
from orders order by 2