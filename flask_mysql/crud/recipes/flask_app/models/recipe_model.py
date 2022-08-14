from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Recipes:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made'].strftime('%b %d %Y')
        self.cook_time = data['cook_time']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        
    @classmethod
    def all_recipes(cls):
        query = "SELECT * from recipes join users on users.id = recipes.user_id"
        results = connectToMySQL('recipes').query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def Update_recipe(cls,data):
        query= "UPDATE recipes set name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, cook_time = %(cook_time)s where recipes.id = %(id)s"
        return connectToMySQL('recipes').query_db(query,data)
    
    @classmethod
    def get_one_recipe(cls,data):
        query = "SELECT * from recipes join users on users.id = recipes.user_id where recipes.id = %(id)s"
        results = connectToMySQL('recipes').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def create_recipe(cls, data):
        query = "INSERT Into recipes(name, description, instructions, date_made, cook_time, user_id) values (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(cook_time)s, %(user_id)s)"
        return connectToMySQL('recipes').query_db(query,data)
    
    @classmethod
    def delete_post(cls,data):
        query = "DELETE From recipes where recipes.id = %(id)s"
        return connectToMySQL('recipes').query_db(query,data)
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) <= 0 or len(recipe['description']) <= 0 or len(recipe['instructions']) <= 0 or len(recipe['date_made']) <= 0 or len(recipe['cook_time']) <= 0:
            is_valid = False
            flash('All fields are required', 'create')
            return is_valid
        if len(recipe['name']) <= 3:
            is_valid = False
            flash("Name must be atleast 3 characters","create")
        if len(recipe['description']) <= 3:
            is_valid = False
            flash("Description must be atleast 3 characters","create")
        if len(recipe['instructions']) <= 3:
            is_valid = False
            flash("Instructions must be atleast 3 characters","create")
        return is_valid
