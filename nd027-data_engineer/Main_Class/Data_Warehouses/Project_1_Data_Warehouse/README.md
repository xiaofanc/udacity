# Project: Data Modeling with Postgres
## Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Schema for Song Play Analysis
Using the song and log datasets(json), you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

### Fact Table
1.**songplays** - records in log data associated with song plays i.e. records with page NextSong (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
### Dimension Tables
2.**users** - users in the app (user_id, first_name, last_name, gender, level)   
3.**songs** - songs in music database (song_id, title, artist_id, year, duration)  
4.**artists** - artists in music database (artist_id, name, location, latitude, longitude)  
5.**time** - timestamps of records in songplays broken down into specific units (start_time, hour, day, week, month, year, weekday)

## Project Template
1.**create_table.py** is where you'll create your fact and dimension tables for the star schema in Redshift.
2.**etl.py** is where you'll load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.
3.**sql_queries.py** is where you'll define you SQL statements, which will be imported into the two other files above.
4.**README.md** is where you'll provide discussion on your process and decisions for this ETL pipeline.

## Project Steps
### Create Tables
* Write CREATE/DROP statements in sql_queries.py to specify all columns for each of the five tables with the right data types and conditions
* Complete the logic in create_tables.py to connect to the database and create these tables
* Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.
* Launch a redshift cluster and create an IAM role that has read access to S3.
* Add redshift database and IAM role info to dwh.cfg.
* Test by running create_tables.py and checking the table schemas in your redshift database. You can use Query Editor in the AWS Redshift console for this.

### Build ETL Pipeline
* Implement the logic in etl.py to load data from S3 to staging tables on Redshift.
* Implement the logic in etl.py to load data from staging tables to analytics tables on Redshift.
* Test by running etl.py after running create_tables.py and running the analytic queries on your Redshift database to compare your results with the expected results.
* Delete your redshift cluster when finished.

### Final
* Run etl in console, and verify results: Python3 create_tables.py && python3 etl.py
