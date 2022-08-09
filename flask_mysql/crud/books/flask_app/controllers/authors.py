from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.author import Authors
from flask_app.models.book import Books


@app.route('/')
def default():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template("authors.html", all_authors= Authors.get_all_authors())

@app.route('/author/create', methods=['POST'])
def create_author():
    new_id = Authors.save_authors(request.form)
    print(new_id)
    return redirect('/authors')

@app.route('/authors/<int:author_id>')
def show_author(author_id):
    data = {
        'id': author_id
    }
    return render_template('author.html', author=Authors.get_one_author(data), new_books=Books.unfavorite_books(data))

@app.route('/author/favorite/<int:author_id>', methods=['POST'])
def add_favorite_book(author_id):
    data = {
        'book_id': request.form['book_id'],
        'author_id': author_id
    }
    Authors.add_favorite_book(data)
    return redirect(f"/authors/{author_id}")
