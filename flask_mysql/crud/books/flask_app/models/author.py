from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Authors:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.books = []

    @classmethod
    def get_all_authors(cls):
        query = 'SELECT * from authors'
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def save_authors(cls, data):
        query = "INSERT INTO authors(name) values (%(new_author)s);"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_one_author(cls, data):
        query = "SELECT * from authors left join favorites on favorites.author_id = authors.id left join books on favorites.book_id = books.id where authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        author = cls(results[0])
        for row in results:
            book_data = {
                'id': row['id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages']
            }
            author.books.append(book.Books(book_data))
        return author
    
    @classmethod
    def unfavorite_author(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        results = connectToMySQL('books_schema').query_db(query,data)
        author_list = []
        for row in results:
            author_data = {
                'id': row['id'],
                'name': row['name']
            }
            author_list.append(cls(author_data))
        return author_list
    
    @classmethod
    def add_favorite_book(cls,data):
        query = "INSERT into favorites(author_id, book_id) values (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query, data)