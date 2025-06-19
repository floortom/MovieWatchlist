import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    releaseTimestamp REAL,
    watched INTEGER
);"""

INSERT_MOVIES = """INSERT INTO movies (title, releaseTimestamp, watched)
    VALUES (?, ?, 0);"""
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE releaseTimestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"
WATCH_MOVIE = "UPDATE movies SET watched = 1 WHERE title = ?;"


connection = sqlite3.connect("Movies.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)


def add_movie(title, releaseTimestamp):
    with connection:
        connection.execute(INSERT_MOVIES,
                           (title, releaseTimestamp))


def get_movies(upcoming=False):
    cursor = connection.cursor()
    if upcoming:
        todayTimestamp = datetime.datetime.today().timestamp()
        cursor.execute(SELECT_UPCOMING_MOVIES,
                       (todayTimestamp,))
    else:
        cursor.execute(SELECT_ALL_MOVIES)
    return cursor.fetchall()


def watch_movie(title):
    with connection:
        connection.execute(WATCH_MOVIE,
                           (title,))


def get_watched_movies():
    with connection:
        return connection.execute(SELECT_WATCHED_MOVIES)
