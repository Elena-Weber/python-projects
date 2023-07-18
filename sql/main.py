from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

all_books = []

db = sqlite3.connect("books_db.db") # this will create database on its own automatically
cursor = db.cursor() # this helps interact with db

# cursor.execute("CREATE TABLE books_table (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books_table VALUES(1, 'Harry Potter 1', 'J.K.Rowling', '6.1')")
# cursor.execute("INSERT INTO books_table VALUES(2, 'Harry Potter 2', 'J.K.Rowling', '7.5')")
# cursor.execute("INSERT INTO books_table VALUES(3, 'Harry Potter 3', 'J.K.Rowling', '4.8')")

# db.commit() # .commit is NOT NEEDED for INSERT

@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', "GET"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)