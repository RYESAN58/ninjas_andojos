from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.name = db_data['Name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the burgers that are associated with a restaurant.
        self.ninjas = []
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('dojos_ninjas').query_db(query,data)
    @classmethod
    def get_dojos_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls( results[0] )
        for row_from_db in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "name" : row_from_db["ninjas.firstname"],
                "bun" : row_from_db["ninjas.lastname"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        x = []
        for i in results:
            x.append( cls(i) )
        return x