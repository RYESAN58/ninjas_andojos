from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        x = []
        for i in results:
            x.append( cls(i) )
        return x
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('dojos_ninjas').query_db( query, data)
    @classmethod
    def remove(cls, num ):
        query = f"DELETE FROM `ninjas`.`user` WHERE (`id` = {num});"
        return connectToMySQL('dojos_ninjas').query_db(query)
    @classmethod
    def update(cls, data):
        query= "UPDATE `ninjas`.`dojos_ninjas` SET `first_name` = %(fname)s, `last_name` = %(lname)s, `email` = %(email)s WHERE (`id` =  %(id)s);"
        return connectToMySQL('dojos_ninjas').query_db( query,data)