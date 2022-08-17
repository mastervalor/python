from flask_app.config.mysqlconnection import connectToMySQL

class Likes:
    db ='belt_exam'
    def __init__(self,data):
        self.user_id = data['user_id']
        self.show_id = data['show_id']

    @classmethod
    def likes(cls, data):
        query = "SELECT * from likes where show_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        likes = 0
        for row in results:
            likes += 1
        return likes