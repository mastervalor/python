from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data ['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users(first_name, last_name, email) VALUES ( %(fname)s, %(lname)s, %(email)s);"
        return connectToMySQL('users').query_db( query, data)
    
    @classmethod
    def updated(cls,data):
        query = "update users set first_name=%(fname)s, last_name=%(lname)s, email=%(email)s where id = %(id)s"
        return connectToMySQL('users').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_one(cls, user_id):
        query = "SELECT * from users where id = %(id)s"
        results = connectToMySQL('users').query_db(query, user_id)
        return cls(results[0])
    
    @classmethod
    def delete(cls,user_id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        retults = connectToMySQL('users').query_db(query, user_id)
        print(retults)
        
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['fname']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['lname']) < 2:
            flash("Last name must be at least 2 characters")
            is_valid = False
        if len(user['email']) < 2:
            flash("Email is required")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invald email address")
            is_valid = False
        return is_valid