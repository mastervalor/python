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
    
    @classmethod
    def add_languages(cls,data):
        query = "INSERT into favorites(language_id, user_id) values (%(language_id)s, %(user_id)s);"
        return connectToMySQL('login').query_db(query, data)
    
    @classmethod
    def get_languages_by_user_id(cls,data):
        query = "SELECT * from languages left join favorites on favorites.language_id = languages.id where favorites.user_id = %(id)s;"
        results = connectToMySQL('login').query_db(query,data)
        language = []
        for row in results:
            language_data = {
                'id': row['id'],
                'language': row['language']
            }
            language.append(cls(language_data))
        return language