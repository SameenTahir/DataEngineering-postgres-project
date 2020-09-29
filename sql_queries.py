# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs 
                            (
                            song_id varchar PRIMARY KEY, 
                            title varchar, 
                            artist_id varchar,
                            year varchar,
                            duration float
                            );""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists
                            (
                            artist_id varchar PRIMARY KEY,
                            name varchar, 
                            location varchar,
                            latitude varchar,
                            longitude varchar
                            );""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time 
                            (
                            start_time time PRIMARY KEY, 
                            hour int, 
                            day int,
                            week int,
                            month int,
                            year int,
                            dayofweek int)
                            ;""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users 
                            (
                            userId varchar PRIMARY KEY, 
                            firstName varchar, 
                            lastName varchar,
                            gender varchar,
                            level varchar
                            );""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays 
                            (
                            songplay_id serial PRIMARY KEY, 
                            ts timestamp NOT NULL, 
                            userId varchar NOT NULL, 
                            level varchar, 
                            song_id varchar, 
                            artist_id varchar, 
                            session_id int, 
                            artist_location varchar, 
                            user_agent varchar,
                            CONSTRAINT userId
                                FOREIGN KEY (userId)
                                    REFERENCES users(userId),
                            CONSTRAINT song_id
                                FOREIGN KEY (song_id)
                                    REFERENCES songs(song_id),
                            CONSTRAINT artist_id
                                FOREIGN KEY (artist_id)
                                    REFERENCES artists(artist_id)
                            );""")

# INSERT RECORDS

song_table_insert = ("""INSERT INTO songs (song_id,title,artist_id,year,duration)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (song_id) DO NOTHING """)
artist_table_insert = ("""INSERT INTO artists (artist_id,name,location,latitude,longitude)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (artist_id) DO NOTHING """)
time_table_insert = ("""INSERT INTO time (start_time,hour,day,week,month,year,dayofweek)
                            VALUES (%s, %s, %s, %s, %s,%s,%s)
                            ON CONFLICT (start_time) DO NOTHING """)
user_table_insert = ("""INSERT INTO users (userId,firstName,lastName,gender,level)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (userId) DO UPDATE 
                            SET level=excluded.level """)
songplay_table_insert = ("""
INSERT INTO songplays (
        ts,
        userId,
        level,
        song_id,
        artist_id,
        session_id,
        artist_location,
        user_agent)
        VALUES (TO_TIMESTAMP(%s), %s, %s, %s, %s, %s, %s, %s)
        ;
""")
# FIND SONGS

song_select = (""" SELECT songs.song_id, artists.artist_id FROM songs 
JOIN artists ON (songs.artist_id = artists.artist_id) 
WHERE (songs.title = %s AND artists.name = %s AND songs.duration = %s)

""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop,songplay_table_drop]