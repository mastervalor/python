from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookie:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.box_count = data['box_count']

    @classmethod
    def save(cls, data):
        query = "INSERT into cookies(customer_name, cookie_type, box_count) values (%(name)s, %(cookie)s, %(boxes)s);"
        return connectToMySQL('cookies').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookies;"
        results = connectToMySQL('cookies').query_db(query)
        all_cookies = []
        for cookie in results:
            all_cookies.append(cls(cookie))
        return all_cookies
    
    @classmethod
    def updated(cls,data):
        query = "update cookies set customer_name=%(name)s, cookie_type=%(cookie)s, box_count=%(boxes)s where id = %(id)s"
        return connectToMySQL('cookies').query_db(query, data)
    
    @classmethod
    def get_one(cls,cookie_id):
        query = "SELECT * from cookies where id= %(id)s"
        results = connectToMySQL('cookies').query_db(query, cookie_id)
        return cls(results[0])
    
    @staticmethod
    def validate_cookie(cookie):
        is_valid = True
        if len(cookie["name"]) <= 0 or len(cookie["cookie"]) <= 0 or len(cookie["boxes"]) <= 0:
            valid = False
            flash("All fields required")
            return valid
        if len(cookie['name']) < 2:
            flash("Customer name must be at least 2 characters.")
            is_valid = False
        if len(cookie['cookie']) < 2:
            flash("Cookie type must be at least 2 characters")
            is_valid = False
        if int(cookie['boxes']) <= 0:
            flash("Number of boxed must be more the 0")
            is_valid = False
        return is_valid