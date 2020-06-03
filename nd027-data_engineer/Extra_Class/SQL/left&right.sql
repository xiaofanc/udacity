left(phone_number, 3) as area_code
right(phone_number, 8) as phone_only 
right(phone_number, length(phone_number)) as phone_only

--In the accounts table, there is a column holding the website for each company. The last three digits specify what type of web address they are using. A list of extensions (and pricing) is provided here. Pull these extensions and provide how many of each website type exist in the accounts table.

select count(distinct right(website, 3))as type from accounts


--There is much debate about how much the name (or even the first letter of a company name) matters. Use the accounts table to pull the first letter of each company name to see the distribution of company names that begin with each letter (or number).
 
select left(name, 1) as type, count(*) from accounts
group by 1
order by 2 desc

--Use the accounts table and a CASE statement to create two groups: one group of company names that start with a number and a second group of those company names that start with a letter. What proportion of company names start with a letter?


select sum(num) nums, sum(alpha) alphas from (
    select name, 
    (left(name, 1) ~  '\d')::integer as num,
    (left(name, 1) ~ '[^\d]')::integer as alpha
    from accounts
) t

select avg(num) nums, avg(alpha) alphas from (
    select name, 
    (left(name, 1) ~  '\d')::integer as num,
    (left(name, 1) ~ '[^\d]')::integer as alpha
    from accounts
) t

select sum(num) nums, sum(alpha) alphas from (
    select name, 
    case when left(name, 1) ~ '[0-9]' then 1 else 0 end as num,
    case when left(name, 1) ~ '[^0-9]' then 1 else 0 end as alpha
    from accounts
) t

select sum(num) nums, sum(alpha) alphas from (
    select name, 
    case when left(lower(name), 1) ~ '[a-z]' then 1 else 0 end as alpha,
    case when left(lower(name), 1) ~ '[^a-z]' then 1 else 0 end as num
    from accounts
) t


--Consider vowels as a, e, i, o, and u. What proportion of company names start with a vowel, and what percent start with anything else?

select sum(vowels) vols, sum(consonant) consonants from (
    select name, 
    (left(name, 1) ~  '[aeiouAEIOU]')::integer as vowels,
    (left(name, 1) ~ '[^aeiouAEIOU]')::integer as consonant
    from accounts
) t


