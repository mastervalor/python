from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Books:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data ['num_of_pages']
        self.authors = []

    @classmethod
    def get_all_books(cls):
        query = "SELECT * from books"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def save_book(cls, data):
        query = "INSERT INTO books(title,num_of_pages) values (%(new_book)s, %(new_book_pages)s);"
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def get_books_favorites(cls, data):
        query = "SELECT * from books left join favorites on favorites.book_id = books.id left join authors on favorites.author_id = authors.id where books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        print(results)
        book = cls(results[0])
        for row in results:
            author_data = {
                'id': row['id'],
                'name': row['name']
            }
            book.authors.append(author.Authors(author_data))
        return book
    
    @classmethod
    def unfavorite_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('books_schema').query_db(query,data)
        books_list = []
        for row in results:
            book_data = {
                'id': row['id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages']
            }
            books_list.append(cls(book_data))
        return books_list
    
    @classmethod
    def add_favorite_author(cls,data):
        query = "INSERT into favorites(author_id, book_id) values (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data)