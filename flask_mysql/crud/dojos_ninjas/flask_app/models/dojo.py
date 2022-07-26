from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninjas

class Dojos:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        
    @classmethod
    def get_all(cls):
        query = "select * from dojos"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name) VALUES (%(new_dojo)s);"
        return connectToMySQL('dojos_ninjas').query_db(query,data)
    
    @classmethod
    def get_dojos_with_ninjas(cls, data):
        query = "SELECT * FROM dojos left join ninjas on ninjas.dojo_id = dojos.id where dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, data)
        dojo_ninjas = cls(results[0])
        for dojo in results:
            dojo_ninjas.ninjas.append(Ninjas.get_one({'id':dojo['ninjas.id']}))
        return dojo_ninjas