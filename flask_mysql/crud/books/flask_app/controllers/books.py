from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.book import Books
from flask_app.models.author import Authors


@app.route('/books')
def books():
    return render_template("books.html", all_books=Books.get_all_books())

@app.route('/book/create', methods=['POST'])
def create_book():
    Books.save_book(request.form)
    return redirect('/books')

@app.route('/books/<int:book_id>')
def show_book(book_id):
    data = {
        'id': book_id
    }
    return render_template('book.html', book=Books.get_books_favorites(data), new_author=Authors.unfavorite_author(data))

@app.route('/book/favorite/<int:book_id>', methods=['POST'])
def add_favorite_auhtor(book_id):
    data = {
        'book_id': book_id,
        'author_id': request.form['author_id']
    }
    Books.add_favorite_author(data)
    return redirect(f"/books/{book_id}")