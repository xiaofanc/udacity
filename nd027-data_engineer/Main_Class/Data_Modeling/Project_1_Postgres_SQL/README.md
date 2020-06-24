# Project: Data Modeling with Postgres
## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. 

You need to create a database schema and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Schema for Song Play Analysis
Using the song and log datasets(json), you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

### Fact Table
1.**songplays** - records in log data associated with song plays i.e. records with page NextSong (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
### Dimension Tables
2.**users** - users in the app (user_id, first_name, last_name, gender, level)
3.**songs** - songs in music database (song_id, title, artist_id, year, duration)
4.**artists** - artists in music database (artist_id, name, location, latitude, longitude)
5.**time** - timestamps of records in songplays broken down into specific units (start_time, hour, day, week, month, year, weekday)

## Project Steps
### Create Tables
* Write CREATE/DROP statements in sql_queries.py to specify all columns for each of the five tables with the right data types and conditions
* Run create_tables.py to connect to the Sparkify database, drops any tables if they exist, and creates the tables
* Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.

### Build ETL Processes
* etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
* Follow instructions in the etl.ipynb notebook to develop ETL processes for each table. 
* run test.ipynb to confirm that records were successfully inserted into each table. Remember to rerun create_tables.py to reset your tables before each time you run this notebook.

### Build ETL Pipeline
* The script etl.py connects to the Sparkify database, extracts and processes the log_data and song_data, and loads data into the five tables.
* Follow instructions in the etl.py notebook to develop ETL processes for each table. 
* run test.ipynb to confirm that records were successfully inserted into each table. Remember to rerun create_tables.py to reset your tables before each time you run this notebook.

### Final
* Run etl in console, and verify results: Python3 create_tables.py && python3 etl.py
