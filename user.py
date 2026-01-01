class User:
    def __init__(self, data):
        self.data = data

    def show_movies(self):
        for i, m in enumerate(self.data.movies, 1):
            print(f"{i}. {m.name} ({m.category}) - Rs {m.price} - Seats {m.seats}")

    def book_ticket(self):
        self.show_movies()
        ch = int(input("Choose movie: "))
        qty = int(input("Tickets: "))
        movie = self.data.movies[ch - 1]

        if qty <= movie.seats:
            movie.seats -= qty
            total = qty * movie.price
            with open("bookings.txt", "a") as f:
                f.write(f"{movie.name},{qty},{total}\n")
            self.data.save_movies()
            print("Booked! Total:", total)
        else:
            print("Not enough seats!")