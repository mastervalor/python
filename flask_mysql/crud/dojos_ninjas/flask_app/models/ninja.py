from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        
    @classmethod
    def get_all(cls):
        query = "select * from ninjas"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * from ninjas where id = %(id)s;"
        ninja = connectToMySQL('dojos_ninjas').query_db(query, data)
        return cls(ninja[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_name)s);"
        return connectToMySQL('dojos_ninjas').query_db(query,data)