
# compare current row with previous row or next row

select account_id,
    standard_sum,
    LAG(standard_sum) OVER (ORDER BY standard_sum) as lag,
    LEAD(standard_sum) OVER (ORDER BY standard_sum) as lead,
    standard_sum - LAG(standard_sum) OVER (ORDER BY standard_sum) as lag_diff,
    standard_sum - LEAD(standard_sum) OVER (ORDER BY standard_sum) as lead_diff
from (
    select account_id,
           sum(standard_qty)) as standard_sum
    from orders
    group by 1 ) sub


SELECT account_id,
       standard_sum,
       LAG(standard_sum) OVER main_window AS lag,
       LEAD(standard_sum) OVER main_window AS lead,
       standard_sum - LAG(standard_sum) OVER main_window AS lag_difference,
       LEAD(standard_sum) OVER main_window - standard_sum AS lead_difference
FROM (
SELECT account_id,
       SUM(standard_qty) AS standard_sum
  FROM orders 
 GROUP BY 1
 ) sub

WINDOW main_window as (ORDER BY standard_sum)