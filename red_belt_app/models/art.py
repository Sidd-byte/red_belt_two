from red_belt_app.config.mysqlconnection import connectToMySQL
from flask import flash
from red_belt_app.models import user


class Show:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.created_at = data['created_at']

    @staticmethod
    def validate_show(form_data):
        is_valid= True
        if len(form_data['title']) < 3:
            flash("Your title must be longer than three letters","title")
            is_valid= False
        if form_data['price'] == "":
            flash("price must be given","price")
            is_valid= False
        if len(form_data['description']) < 3:
            flash("Your description must be longer than three letters","description")
            is_valid= False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO art (user_id, title, price, description) VALUES (%(user_id)s,%(title)s,%(price)s,%(description)s);"
        new_art_id = connectToMySQL('users_n_art').query_db(query,data)
        return new_art_id

    @classmethod
    def getall(cls):
        query = "SELECT * FROM art JOIN users ON users.id = art.user_id"
        results = connectToMySQL('users_n_art').query_db(query)
        arts = []
        for row in results:
            art = cls(results[0])
            data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password': row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            art.poster = user.User(data)
            arts.append(art)
        print(arts)
        return arts

    @classmethod
    def get_art(cls, data):
        query = "SELECT * FROM art WHERE id = %(id)s;"
        results = connectToMySQL('users_n_art').query_db(query, data)
        return cls(results[0])


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM art WHERE id = %(id)s;"
        connectToMySQL('users_n_art').query_db(query,data)