
concat(first, ' ', last) as full_name
first || ' ' || last as name

--Each company in the accounts table wants to create an email address for each primary_poc. The email address should be the first name of the primary_poc . last name primary_poc @ company name .com.

select primary_poc,
    strpos(primary_poc, ' ') as blank,
    left(primary_poc, strpos(primary_poc, ' ')-1) as first_name,
    right(primary_poc, length(primary_poc) - strpos(primary_poc, ' ')) as last_name,
    concat(left(primary_poc, strpos(primary_poc, ' ')-1), '.', right(primary_poc, 
    length(primary_poc) - strpos(primary_poc, ' ')), '@', name, '.com') as add
from accounts 

--You may have noticed that in the previous solution some of the company names include spaces, which will certainly not work in an email address. See if you can create an email address that will work by removing all of the spaces in the account name, but otherwise your solution should be just as in question 1. Some helpful documentation is here.

with temp as (
select primary_poc,
    strpos(primary_poc, ' ') as blank,
    left(primary_poc, strpos(primary_poc, ' ')-1) as first_name,
    right(primary_poc, length(primary_poc) - strpos(primary_poc, ' ')) as last_name,
    name from accounts)

select first_name, last_name,
       concat(first_name, '.', last_name, '@', replace(name, ' ',''), '.com') as add
from temp 

select concat(replace(primary_poc, ' ', '.', '@'), replace(name, ' ',''), '.com') as 
email from accounts

--We would also like to create an initial password, which they will change after their first log in. The first password will be the first letter of the primary_poc's first name (lowercase), then the last letter of their first name (lowercase), the first letter of their last name (lowercase), the last letter of their last name (lowercase), the number of letters in their first name, the number of letters in their last name, and then the name of the company they are working with, all capitalized with no spaces.

with temp as (
select primary_poc,
    strpos(primary_poc, ' ') as blank,
    left(primary_poc, strpos(primary_poc, ' ')-1) as first_name,
    right(primary_poc, length(primary_poc) - strpos(primary_poc, ' ')) as last_name,
    name from accounts)

# concat will automatically transform int to string or using varchar/text

select concat(left(lower(first_name), 1), right(lower(first_name), 1), left(lower(last_name), 1), right(lower(last_name), 1), length(first_name)::varchar, length(last_name)::varchar, replace(upper(name), ' ', '')) as pwd from temp

select concat(left(lower(first_name), 1), right(lower(first_name), 1), left(lower(last_name), 1), right(lower(last_name), 1), length(first_name)::text, length(last_name)::varchar, replace(upper(name), ' ', '')) as pwd from temp




