import datetime
import database as db

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user to the app.
7) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
db.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    releaseDate = input("Release date (dd-mm-YYYY): ")
    parsedTime = datetime.datetime.strptime(releaseDate, "%d-%m-%Y")
    timeStamp = parsedTime.timestamp()
    db.add_movie(title, timeStamp)


def prompt_watch_movie():
    username = input("Username: ")
    movID = input("Enter the watched movie ID: ")
    db.watch_movie(username, movID)


def prompt_add_user():
    username = input("Username: ")
    db.add_user(username)


def prompt_show_watched():
    username = input("Username: ")
    watched = db.get_watched_movies(username)
    if watched:
        print_movies("Watched", watched)
    else:
        print("That user has watched no movies yet.")


def print_movies(heading, movies):
    print(f"--- {heading} movies ---")
    for _id, title, releaseDate in movies:
        movDate = datetime.datetime.fromtimestamp(releaseDate)
        humanDate = movDate.strftime("%d %b %Y")
        print(f"{_id}: {title} ({humanDate})")
    print("---" * 6, "\n")


# def print_watched_movie_list(username, movies):
#     print(f"--- {username}'s watched movies ---")
#     for movie in movies:
#         print(f"{movie[1]}")
#     print("---" * 6, "\n")


while (user_input := input(menu)) != "7":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        upcoming = db.get_movies(True)
        print_movies("Upcoming", upcoming)
    elif user_input == "3":
        movies = db.get_movies()
        print_movies("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched()
    elif user_input == "6":
        prompt_add_user()
    else:
        print("Invalid input, please try again!")
