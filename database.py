import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    releaseTimestamp REAL
);"""

CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    watcherName TEXT,
    title TEXT
);"""

INSERT_MOVIES = """INSERT INTO movies (title, releaseTimestamp)
    VALUES (?, ?);"""
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE releaseTimestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcherName = ?;"
INSERT_WATCHED_MOVIES = """INSERT INTO watched (watcherName, title);
    VALUES (?, ?);"""
# WATCH_MOVIE = "UPDATE movies SET watched = 1 WHERE title = ?;"



connection = sqlite3.connect("Movies.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHLIST_TABLE)


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


def watch_movie(username, title):
    with connection:
        connection.execute(DELETE_MOVIE,
                           (title,))
        connection.execute(INSERT_WATCHED_MOVIES,
                           (username, title))


def get_watched_movies(username):
    with connection:
        return connection.execute(SELECT_WATCHED_MOVIES,
                                  (username,))
