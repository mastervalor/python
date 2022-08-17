from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model

class Shows:
    db = 'belt_exam'
    def __init__(self,data):
        self.id = data['id']
        self.title = data ['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.poster_id = data['poster_id']
        self.users = []
        
    @classmethod
    def all_shows(cls):
        query = "SELECT * from shows join users on users.id = shows.poster_id"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def get_one_show(cls,data):
        query = "SELECT * from shows join users on users.id = shows.poster_id where shows.id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        show = cls(results[0])
        for row in results:
            user_data = {
                'id': row['id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row ['password']
            }
            show.users.append(user_model.Users(user_data))
        return show
    
    @classmethod
    def create_show(cls, data):
        query = "INSERT Into shows(title, description, release_date, network, poster_id) values (%(title)s, %(description)s, %(release_date)s, %(network)s, %(poster_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def Update_show(cls,data):
        query= "UPDATE shows set title = %(title)s, description = %(description)s, release_date = %(release_date)s, network = %(network)s where shows.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete_show(cls,data):
        query = "DELETE From shows where shows.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def unfavored_show (cls,data):
        query = "SELECT * FROM shows WHERE shows.id NOT IN ( SELECT show_id FROM likes WHERE user_id = %(id)s );"
        results = connectToMySQL(cls.db).query_db(query,data)
        shows_list = []
        for row in results:
            show_data = {
                'id': row['id'],
                'title': row['title'],
                'network': row['network'],
                'release_date': row['release_date'],
                'description': row['description'],
                'poster_id': row['poster_id']
            }
            shows_list.append(cls(show_data))
        return shows_list
    
    @classmethod
    def favored_show (cls,data):
        query = "SELECT * FROM shows WHERE shows.id IN ( SELECT show_id FROM likes WHERE user_id = %(id)s );"
        results = connectToMySQL(cls.db).query_db(query,data)
        shows_list = []
        for row in results:
            show_data = {
                'id': row['id'],
                'title': row['title'],
                'network': row['network'],
                'release_date': row['release_date'],
                'description': row['description'],
                'poster_id': row['poster_id']
            }
            shows_list.append(cls(show_data))
        return shows_list
    
    @classmethod
    def like_show(cls,data):
        query = "INSERT into likes(show_id, user_id) values (%(show_id)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def unlike_show(cls,data):
        query = "DELETE from likes where show_id = %(show_id)s and user_id = %(user_id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @staticmethod
    def validate_show(show):
        is_valid = True
        if len(show['title']) <= 0 or len(show['description']) <= 0 or len(show['network']) <= 0 or len(show['release_date']) <= 0:
            is_valid = False
            flash('All fields are required', 'create')
            return is_valid
        if len(show['title']) <= 3:
            is_valid = False
            flash("Title must be atleast 3 characters","create")
        if len(show['description']) <= 3:
            is_valid = False
            flash("Description must be atleast 3 characters","create")
        if len(show['network']) <= 3:
            print(len(show['network']))
            is_valid = False
            flash("Network must be atleast 3 characters","create")
        return is_valid