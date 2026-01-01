# main.py

from data import MovieData
from admin import Admin
from user import User

data = MovieData()
admin = Admin(data)
user = User(data)

while True:
    print("\n1. Admin Mode\n2. User Mode\n3. Exit")
    ch = input("Choose: ")

    if ch == "1":
        print("1.View 2.Add 3.Remove")
        a = input("Choice: ")
        if a == "1": admin.view_movies()
        elif a == "2": admin.add_movie()
        elif a == "3": admin.remove_movie()

    elif ch == "2":
        user.book_ticket()

    elif ch == "3":
        break
