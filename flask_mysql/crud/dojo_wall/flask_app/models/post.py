from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
import datetime

class Posts:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at'].strftime('%b %d')
        self.user_id = data['user_id']
        self.user_name = data['first_name']
        
    @classmethod
    def get_all_posts(cls):
        query = "select * from posts join users on users.id = posts.user_id"
        results = connectToMySQL('dojo_wall').query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def create_post(cls, data):
        query = "INSERT Into posts(content, user_id) values (%(content)s, %(user_id)s)"
        return connectToMySQL('dojo_wall').query_db(query,data)
    
    @classmethod
    def delete_post(cls,data):
        query = "DELETE From posts where posts.id = %(id)s"
        return connectToMySQL('dojo_wall').query_db(query,data)