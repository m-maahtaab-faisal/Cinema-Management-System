# data.py

class Movie:
    def __init__(self, name, category, time, price, seats):
        self.name = name
        self.category = category
        self.time = time
        self.price = int(price)
        self.seats = int(seats)

    def to_line(self):
        return f"{self.name},{self.category},{self.time},{self.price},{self.seats}"


class MovieData:
    def __init__(self):
        self.movies = []
        self.load_movies()

    def load_movies(self):
        try:
            with open("movies.txt", "r") as f:
                for line in f:
                    n, c, t, p, s = line.strip().split(",")
                    self.movies.append(Movie(n, c, t, p, s))
        except:
            pass

    def save_movies(self):
        with open("movies.txt", "w") as f:
            for m in self.movies:
                f.write(m.to_line() + "\n")

