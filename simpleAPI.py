# -*- coding: utf-8 -*-
"""
@author: ravi83
"""

from flask import Flask

app = Flask(__name__)

"""if we set route to “/” the code will be executed if we access localhost:5000/.
 You could set the route to “/hello” and our “hello world” will be shown if we access localhost:5000/hello.
"""
@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True) #app will being run if we run from app.py.
    
#build simple restful api with flask and SQLite that have capabilities to create, read, update, and delete data from database.
    
    