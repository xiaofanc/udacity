UNION - stack

UNION removes duplicate rows.
UNION ALL does not remove duplicate rows.

Both tables must have the same number of columns.
Those columns must have the same data types in the same order as the first table.


select * from accounts 
UNION ALL
select * from accounts


select * from accounts 
where name = 'Walmart'
UNION ALL
select * from accounts
where name = 'Disney'


Performing Operations on a Combined Dataset
--Perform the union in your first query (under the Appending Data via UNION header) in a common table expression and name it double_accounts. Then do a COUNT the number of times a name appears in the double_accounts table. If you do this correctly, your query results should have a count of 2 for each name.
with double_accounts as (
select * from accounts 
UNION ALL
select * from accounts )

select name, count(*) from double_accounts group by 1


