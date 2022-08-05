from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.language import Languages
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-aA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}+$')

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.birthdate = data['birthdate']
        self.age = data['age']
        self.gender = data['location']
        self.language = []
        
    @classmethod
    def get_language_by_users(cls, data):
        query = "SELECT * FROM users LEFT JOIN favorites on favorites.user_id = users.id LEFT JOIN languages on favorites.language.id where user.id = %(user)s;"
        results = connectToMySQL('login').query_db(query, data)
        language = cls(results[0])
        for row in results:
            user_data = {
                'id' : row['user.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'birthdate': row['birthdate'],
                'age': row['age'],
                'location': row['location']
            }
            language.for_users.append(user.Users(user_data))
        return language
    
    
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO users(first_name, last_name, email, password, birthdate, age, location) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(birthdate)s, %(age)s, %(location)s);'
        return connectToMySQL('login').query_db(query, data)

    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('login').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) <= 0 or len(user['last_name']) <= 0 or len(user['email']) <= 0 or len(user['password']) <= 0 or len(user['birthdate']) <= 0 or len(user['age']) <= 0 or len(user['location']):
            is_valid = False
            flash('All fields required')
            return is_valid
        if len(user['first_name']) < 2:
            flash('First Name must be at least 2 characters')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last Name must be at least 2 characters')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invald email address')
            is_valid = False
        if not PASSWORD_REGEX.match(user['password']):
            flash('Password must have at least eight characters, at least one uppercase letter, one lowercase letter, one number and one special character')
            is_valid = False
        if user['password_confirm'] != user['password']:
            flash("Passwords don't match")
            is_valid = False
        return is_valid