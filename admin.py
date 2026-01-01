# admin.py

from data import Movie, MovieData

class Admin:
    def __init__(self, data):
        self.data = data

    def view_movies(self):
        print("\n--- MOVIES ---")
        for i, m in enumerate(self.data.movies, 1):
            print(f"{i}. {m.name} | {m.category} | {m.time} | Rs {m.price} | Seats {m.seats}")

    def add_movie(self):
        name = input("Movie name: ")
        cat = input("Category: ")
        time = input("Show time: ")
        price = int(input("Price: "))
        seats = int(input("Seats: "))
        self.data.movies.append(Movie(name, cat, time, price, seats))
        self.data.save_movies()
        print("Movie added!")

    def remove_movie(self):
        self.view_movies()
        ch = int(input("Movie number to remove: "))
        self.data.movies.pop(ch - 1)
        self.data.save_movies()
        print("Movie removed!")
