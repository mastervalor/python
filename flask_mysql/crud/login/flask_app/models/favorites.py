from flask_app.config.mysqlconnection import connectToMySQL


class Favorites:
    def __init__(self, data):
        self.burger_id = data['burger_id']
        self.topping_id = data['topping_id']

    @classmethod
    def save(cls,data):
        query = "INSERT into add_ons(burger_id, topping_id) values (%(burger_id)s, %(topping_id)s);"
        return connectToMySQL('login').query_db(query, data)