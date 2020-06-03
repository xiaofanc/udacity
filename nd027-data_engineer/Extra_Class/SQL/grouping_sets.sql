# group by nothing, group by month, group by country, group by both
%%sql
SELECT d.month, s.country, sum(sales_amount) as revenue
FROM factSales f
JOIN dimDate d ON f.date_key = d.date_key
JOIN dimStore s ON f.store_key = s.store_key
group by grouping sets ((), 1, 2, (1,2))
order by 3 DESC;


CUBE:
# Group by CUBE (dim1, dim2, ..) , produces all combinations of different lenghts in one go.
%%sql
SELECT d.month, s.country, sum(sales_amount) as revenue
FROM factSales f
JOIN dimDate d ON f.date_key = d.date_key
JOIN dimStore s ON f.store_key = s.store_key
group by cube(1, 2)
order by 3 DESC;