
# coalesce replace null value

select count(primary_poc) as regular_count,
       count(coalesce(primary_poc, 'no poc')) as modified_count
from ...


SELECT *,
    coalesce(a.id, o.account_id) as id,
    coalesce(a.id, o.account_id) as account_id,
    coalesce(standard_qty, 0) as standard_qty,
    coalesce(gloss_qty, 0) as gloss_qty,
    coalesce(poster_qty, 0) as poster_qty,
    coalesce(total, 0) as total,
    coalesce(standard_amt_usd, 0) as standard_amt_usd,
    coalesce(gloss_amt_usd, 0) as gloss_amt_usd,
    coalesce(poster_amt_usd, 0) as poster_amt_usd,
    coalesce(total_amt_usd, 0) as total_amt_usd
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id;