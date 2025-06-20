import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    releaseTimestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user TEXT,
    movID INTEGER,
    FOREIGN KEY (user) REFERENCES users(username),
    FOREIGN KEY (movID) REFERENCES movies(id)
);"""

INSERT_MOVIES = """INSERT INTO movies (title, releaseTimestamp)
    VALUES (?, ?);"""
INSERT_USER = "INSERT INTO users (username) VALUES (?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE releaseTimestamp > ?;"
SELECT_WATCHED_MOVIES = """
    SELECT movies.* 
    FROM movies
    JOIN watched ON movies.id = watched.movID
    JOIN users ON users.username = watched.user
    WHERE users.username = ?;"""
INSERT_WATCHED_MOVIES = """INSERT INTO watched (user, movID)
    VALUES (?, ?);"""



connection = sqlite3.connect("Movies.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)


def add_user(username):
    with connection:
        connection.execute(INSERT_USER,
                           (username,))


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


def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIES,
                           (username, movie_id))


def get_watched_movies(username):
    with connection:
        return connection.execute(SELECT_WATCHED_MOVIES,
                                  (username,))
