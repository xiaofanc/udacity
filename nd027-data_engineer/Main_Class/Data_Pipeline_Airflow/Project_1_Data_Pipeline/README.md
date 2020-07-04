# Project: Data Pipeline with Airflow
## Introduction
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

The task is to build high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.


## Project Datasets
* Song data: 's3://udacity-dend/song_data'  
* Log data: 's3://udacity-dend/log_data'  


#### Song Dataset
The first dataset contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.  
* song_data/A/B/C/TRABCEI128F424C983.json  
* song_data/A/A/B/TRAABJL12903CDCF1A.json

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.  
> {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}


#### Log Dataset
The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.  
* log_data/2018/11/2018-11-12-events.json   
* log_data/2018/11/2018-11-13-events.json     

And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.  
> {"artist":null,"auth":"Logged In","firstName":"Walter","gender":"M","itemInSession":0,"lastName":"Frye","length":null,"level":"free","location":"San Francisco-Oakland-Hayward, CA","method":"GET","page":"Home","registration":1540919166796.0,"sessionId":38,"song":null,"status":200,"ts":1541105830796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"39"}


## Project Template
* The **dag template** has all the imports and task templates in place, but the task dependencies have not been set
* The **operators** folder with operator templates
* A **helper class** for the SQL transformations  


## Project Steps
### Create user and launch a redshift cluster on AWS


### Add Airflow Connections
#### Configure AWS credentials
* Conn Id: Enter aws_credentials.  
* Conn Type: Enter Amazon Web Services.  
* Login: Enter your Access key ID from the IAM User credentials you downloaded earlier.  
* Password: Enter your Secret access key from the IAM User credentials you downloaded earlier.  


#### Create Redsift connection
* Conn Id: Enter redshift.  
* Conn Type: Enter Postgres.  
* Host: Enter the endpoint of your Redshift cluster, excluding the port at the end. You can find this by selecting your cluster in the Clusters page of the Amazon Redshift console. See where this is located in the screenshot below. IMPORTANT: Make sure to NOT include the port at the end of the Redshift endpoint string.  
* Schema: Enter dev. This is the Redshift database you want to connect to.  
* Login: Enter awsuser.  
* Password: Enter the password you created when launching your Redshift cluster.
Port: Enter 5439.  


### Configuring the DAG
#### configure the task dependencies



### Building the operators
#### Stage Operator

#### Fact and Dimension Operators

#### Data Quality Operator




### How to run


