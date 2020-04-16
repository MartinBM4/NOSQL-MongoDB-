"""
Solve the following queries using PyMongo and show the results on the screen. Submmit a python file with all the queries.



1. Write a MongoDB query to display all the documents in the collection restaurants.

2. Write a MongoDB query to display all the restaurant which is in the borough Bronx.

3. Write a MongoDB query to find the restaurants who achieved a score more than 90.

4. Write a MongoDB query to find the restaurants which does not prepare any cuisine of 'American ' and achieved a grade point 'A' not belongs to the borough Brooklyn. The document must be displayed according to the cuisine in descending order.


5. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contains 'Reg' as three letters somewhere in its name.

6. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which prepared dish except 'American' and 'Chinees' or restaurant's name begins with letter 'Wil'.

7. Write a MongoDB query which will select all documents in the restaurants collection where the coord field value is Double.
"""





# SOLUTION.


import pymongo
from pymongo import MongoClient

class Explora_Restaurants(object):
    def __init__ (self, url, port, user, password, auth):
        self.url = url
        self.port = port
        self.user = user
        self.password = password
        self.auth = auth
    
    def conectar (self):
        connection = MongoClient(self.url,self.port,username=self.user,password=self.password,authSource=self.auth)
        return connection
    
    def buscar_vecindarios(self, connection):
        db = connection.master
        collection = db.restaurants
        item = collection.find()
        return item
    
    def buscar_bronx(self, connection):
        db = connection.master
        collection = db.restaurants
        item = collection.find({"borough":"Bronx"})
        return item
    
    def puntuacion_mas90(self, connection):
        db = connection.master
        collection = db.restaurants
        item = collection.find({"grades.score": {"$gt": 90}})
        return item
    
    def buscar_grado(self, connection):
        db = connection.master
        collection = db.restaurants
        item = collection.find({"grades.grade": 'A', "cuisine": { "$ne" : 'American'}, 'borough': {"$ne" : 'Brooklyn'}}).sort('cuisine', pymongo.DESCENDING)
        return item
    
    def buscar_por_reg(self, connection):
        db = connection.master
        collection = db.restaurants
        item = collection.find({"name": {"$regex" : ".*Reg.*"}})
        return item
    
    def buscar_por_wil(self, connection):
        db = connection.master
        collection = db.restaurants
        item = collection.find({"$or": [{"cuisine": {"$nin": ["American", "Chinese"]}}, {"name": "^Wil"}]})
        return item
    
    def buscar_coordenadas(self, connection):
        db = connection.master
        collection = db.restaurants
        item = collection.find({"address.coord": {"$type": "double"}})
        return item
    
def get_option():
        print ("1. Una lista de todos los restaurantes.")
        print ("2. Una lista de los restaurantes del barrio Bronx.")
        print ("3. Una lista de los restaurantes con una nota mayor que 90.")
        print ("4. Una lista de los restaurantes de Brooklyn, con un grado A y que no tenga cocina Americana.")
        print ("5. Una lista de los restaurantes que contenga las letras Reg.")
        print ("6. Una lista de los restaurantes que no cocinen comida china o americana y que empiece por las letras Wil.")
        print ("7. Una lista de los restaurantes cuyas coordenadas son del tipo double")
        print ("0. Salir.")

        option = int(input("Seleccione una de las opciones(0-7)"))
        return option
    
option = get_option()
explorer = Explora_Restaurants("localhost", 30000, "master_user", "YVvr3FbHUCCCfT6P", "master")
conn = explorer.conectar()

while option!=0:
    if option == 1:
        result = explorer.buscar_vecindarios(conn)
        print(list(result))
    
    if option == 2:
        result = explorer.buscar_bronx(conn)
        print(list(result))  
        
    if option == 3:
        result = explorer.puntuacion_mas90(conn)
        print(list(result))        
        
    if option == 4:
        result = explorer.buscar_grado(conn)
        print(list(result))        
        
    if option == 5:
        result = explorer.buscar_por_reg(conn)
        print(list(result))        
        
        
    if option == 6:
        result = explorer.buscar_por_wil(conn)
        print(list(result))


    if option == 7:
        result = explorer.buscar_coordenadas(conn)
        print(list(result)) 
    
    option= get_option()