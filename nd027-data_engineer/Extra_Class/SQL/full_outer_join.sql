full outer join

only keep the differences between two tables:
full outer join +
WHERE Table_A.column_name IS NULL OR Table_B.column_name IS NULL

# Finding Matched and Unmatched Rows with FULL OUTER JOIN
--each account who has a sales rep and each sales rep that has an account (all of the columns in these returned rows will be full)

select a.id as c_id, s.id as s_id 
from accounts a inner join sales_reps s 
on a.sales_rep_id = s.id;


--but also each account that does not have a sales rep and each sales rep that does not have an account (some of the columns in these returned rows will be empty)
select a.id as c_id, s.id as s_id 
from accounts a full join sales_reps s 
on a.sales_rep_id = s.id
where a.sales_rep_id is null or s.id is null;

