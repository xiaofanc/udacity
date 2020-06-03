# to_date ('March', 'month') transform string to date
# cast turns string to dates

# month  day  year
# March  12    2012

select *,
    DATE_PART('month', TO_DATE(month, 'month')) as clean_month,
    year || '-' || DATE_PART('month', TO_DATE(month, 'month')) || '-' || day as 
    con_date,
    CAST(year || '-' || DATE_PART('month', TO_DATE(month, 'month')) || '-' || day as 
    date) as formatted_date,
    (year || '-' || DATE_PART('month', TO_DATE(month, 'month')) || '-' || day)::date 
    as formatted_date_alt
from data

-- transform string 'date' to SQL date yyyy-mm-dd
select *, (substr(date,7,4) || '-' || substr(date,1,2) || '-' || 
substr(date,4,2))::date from sf_crime_data limit 10;
