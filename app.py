import datetime
import database as db

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

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


def print_movies(heading, movies):
    print(f"--- {heading} movies ---")
    for movie in movies:
        movDate = datetime.datetime.fromtimestamp(movie[1])
        humanDate = movDate.strftime("%d %b %Y")
        print(f"{movie[0]} ({humanDate})")
    print("---" * 6, "\n")


def prompt_watch_movie():
    title = input("Enter the watched movie title: ")
    db.watch_movie(title)


while (user_input := input(menu)) != "6":
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
        watched = db.get_watched_movies()
        print_movies("Watched", watched)
    else:
        print("Invalid input, please try again!")