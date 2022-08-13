from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, post
import datetime

class Comments:
    def __init__(self,data):
        self.id = data['id']
        self.comment = data['comment']
        self.created_at = data['created_at'].strftime('%b %d')
        self.post_id = data['post_id']
        self.commenter_id = data['commenter_id']
        self.user_name = data['first_name']
        
    @classmethod
    def get_comments_by_post(cls):
        query = "SELECT * from comments join users on users.id = comments.commenter_id join posts on posts.id = comments.post_id"
        results = connectToMySQL('dojo_wall').query_db(query)
        posts = []
        for row in results:
            posts.append(cls(row))
        return posts

    @classmethod
    def create_comment(cls,data):
        query = "INSERT into comments(comment, post_id, commenter_id) values (%(content)s, %(post_id)s, %(commenter_id)s)"
        return connectToMySQL('dojo_wall').query_db(query,data)
    
    @classmethod
    def delete_comment(cls,data):
        query = "DELETE From comments where comments.id = %(id)s"
        return connectToMySQL('dojo_wall').query_db(query,data)