# Data-Modeling-with-Postgres

This project aims to automate the process of creating tables and run queries.

This project creates a postgres database `sparkifydb` for a music app, *Sparkify*. The purpose of the database is to model song and log datasets (originaly stored in JSON format) with a star schema optimised for queries on song play analysis.

## Schema design & ETL pipeline

The star schema has 1 **fact** table (songplays), and 4 *dimension* tables (users, songs, artists, time). 
Queries like: `DROP`, `CREATE`, `INSERT`, and `SELECT` are defined in **sql_queries.py**. **create_tables.py** uses functions `create_database`, `drop_tables`, and `create_tables` to create the database sparkifydb and the required tables.

![](Tables.png?raw=true)

Data from the 'data/song_data' in JSON format are extracted, transformed, and loaded into the songs and artists tables in etl.py.
The "data/log_data" file, which contains processed data from the JSON log files, is what is used to fill the "time" and "users" tables.
In order to fill the **songplays** fact table, a 'SELECT' query gathers song and artist id from the **songs** and **artists** tables and combines this with log file derived data. 

## How To Run the Project

First you have to make sure that postgresql server is running on your machine.

Then you can run `create_tables.py` to create the needed tables.
After that run `etl.py` to feed the tables with data.
