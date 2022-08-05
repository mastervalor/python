from flask_app.config.mysqlconnection import connectToMySQL

class Languages:
    def __init__(self, data):
        self.id = data['id']
        self.language = data['language']
        
    @classmethod
    def get_languages(cls):
        query = "SELECT * FROM languages"
        results = connectToMySQL('login').query_db(query)
        list_of_languages = []
        for result in results:
            list_of_languages.append(cls(result))
        return list_of_languages