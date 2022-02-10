from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['firstname']
        self.last_name = data['lastname']
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
        query = "INSERT INTO ninjas ( firstname , lastname , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('dojos_ninjas').query_db( query, data)
    @classmethod
    def remove(cls, num ):
        query = f"DELETE FROM `ninjas`.`user` WHERE (`id` = {num});"
        return connectToMySQL('dojos_ninjas').query_db(query)
    @classmethod
    def update(cls, data):
        query= "UPDATE `ninjas`.`dojos_ninjas` SET `first_name` = %(fname)s, `last_name` = %(lname)s, `email` = %(email)s WHERE (`id` =  %(id)s);"
        return connectToMySQL('dojos_ninjas').query_db( query,data)
    @classmethod
    def get_dojos(cls, num1):
        query = f"SELECT ninjas.firstname ,ninjas.lastname ,ninjas.dojo_id ,dojos.id, dojos.name FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id = {num1}"
        return connectToMySQL('dojos_ninjas').query_db(query)
    @classmethod
    def add_to_dojo(cls, data):
        query = "INSERT INTO `dojos_ninjas`.`ninjas` (`firstname`, `lastname`, `dojo_id`) VALUES (%(fname)s, %(lname)s,%(dojo_id)s);"
        return connectToMySQL('dojos_ninjas').query_db(query, data)