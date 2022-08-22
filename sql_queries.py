# DROP TABLES
#INSERT INTO songplay
#(songplay_id, start_time, user_id, level, song_id , artist_id , session_id , location , user_agent) VALUES
#(%s,%s,%s,%s,%s,%s,%s,%s,%s),

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS user_table;"
song_table_drop = "DROP TABLE IF EXISTS song_table;"
artist_table_drop = "DROP TABLE IF EXISTS artist_table;"
time_table_drop = "DROP TABLE IF EXISTS time_table;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay 
(songplay_id serial PRIMARY KEY, start_time time, user_id int, level VARCHAR, song_id varchar , artist_id varchar , session_id int, location VARCHAR, user_agent VARCHAR)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS user_table 
(user_id int , first_name varchar, last_name varchar, gender varchar, level varchar)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song_table
(song_id varchar , title varchar, artist_id varchar , year int , duration FLOAT)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist_table
(artist_id varchar, name varchar, location varchar, latitude float, longitude float)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table
(start_time varchar, hour int, day int, week varchar, month int, year int , weekday varchar)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay
(songplay_id , start_time , user_id , level , song_id , artist_id , session_id , location , user_agent ) VALUES
(DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""
INSERT INTO user_table
(user_id , first_name , last_name , gender , level ) VALUES
(%s,%s,%s,%s,%s)
""")

song_table_insert = ("""
INSERT INTO song_table
(song_id , title , artist_id , year , duration) VALUES
(%s,%s,%s,%s,%s)
""")

artist_table_insert = ("""
INSERT INTO artist_table
(artist_id, name, location, latitude, longitude) VALUES
(%s,%s,%s,%s,%s)
""")


time_table_insert = ("""
INSERT INTO time_table
(start_time , hour , day , week , month , year , weekday ) VALUES
(%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS

song_select = ("""
    SELECT song_table.song_id, artist_table.artist_id
    FROM song_table
    JOIN artist_table ON song_table.artist_id = artist_table.artist_id
    WHERE song_table.title = %s AND artist_table.name = %s AND song_table.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]