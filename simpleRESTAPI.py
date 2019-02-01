# -*- coding: utf-8 -*-
"""

@author: ravi83

We will be creating a RESTful API that is used to store users details, which will have CRUD (Create, Read, Update, Delete) functions.
So we can create new user, get details of an existing user and delete existing user.

"""
from flask import Flask #Flask  is the prototype used to create instances of web application or web applications if you want to put it simple.
from flask_restful import Api, Resource, reqparse
app= Flask(__name__) # create an instance for class Flask. By passing _name_ we are telling the app to run in this specific place. Note that _name_ is assigned to _main_ here
api = Api(app) # create an instance for class API

# Create a list of users to simulate a data store:
# Note: This method is used since this article is focusing in creating API, but in actual condition, the data store is usually a database.
users=[{"name": "Sahithya", "age":25, "occupation":"SW"},
       {"name": "Srikanth", "age":26, "occupation":"DL"},
       {"name": "Ravi", "age":40, "occupation":"Bank"}]

class User(Resource):
    
    """Now we will begin creating our API endpoints by defining a User resource class.
       Four functions which correspond to four HTTP request method will be defined and implemented
    """
    def get(self,name):
        """
        The get method is used to retrieve a particular user details by specifying the name
        """
        for user in users:
            if name==user["name"]:
                return user,200
        return "user not found",404
    
    def post(self,name):
        """
        The post method is used to create a new user
        """
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        for user in users:
            if name ==user["name"]:
                return "User already exists",400
        usernew={"name":name,"age":args["age"],"occupation":args["occupation"]}
        users.append(usernew)
        return usernew,201
    
    def put(self,name):
        """
        The put method is used to update details of user, or create a new one if it is not existing yet.
        
        """
        parser=reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args=parser.parse_args()
        for user in users:
            if name==user["name"]:
                user["age"]=args["age"]
                user["occupation"]=args["occupation"]
                return user,200
        usernew={"name":name,"age":args["age"],"occupation":args["occupation"]}
        users.append(usernew)
        return usernew,201
    
    def delete(self,name):
        """
        The delete method is used to delete user that is no longer relevant
        
        """
        for user in users:
            global users
            users=[user for user in users if user["name"]!=name]
            return "deleted",200
        
"""We have done implementing all the methods in our User resource,
   we will add the resource to our API and specify its route, then run our Flask application
   """
api.add_resource(User, "/user/<string:name>")
app.run(debug=True)       
        