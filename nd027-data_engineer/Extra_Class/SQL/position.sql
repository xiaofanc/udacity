select first_name,
       last_name,
       city_state,
       POSITION(',' IN city_states) as comma_p,
       STRPOS(city_states, ',') as substr_comma_p,
       LOWER(city_states) as low,
       UPPER(city_states) as upp,
       LEFT(city_states, POSITION(',' IN city_states)-1) as city
    from customer_date

--Use the accounts table to create first and last name columns that hold the first and last names for the primary_poc.

select primary_poc,
    strpos(primary_poc, ' ') as blank,
    left(primary_poc, strpos(primary_poc, ' ')-1) as first_name,
    right(primary_poc, length(primary_poc) - strpos(primary_poc, ' ')) as last_name
from accounts 

--Now see if you can do the same thing for every rep name in the sales_reps table. Again provide first and last name columns.

select name,
    strpos(name, ' ') as blank,
    left(name, strpos(name, ' ')-1) as first_name,
    right(name, length(name) - strpos(name, ' ')) as last_name
from sales_reps 