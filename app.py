from flask import Flask
import os
from flask_pymongo import Pymongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):  # import file where username and password of MongoDB is saved
    import env

app = Flask(__name__)  # create instance of flask

# add configuration to Flask app
app.config("MONGODB_NAME") = task_manager
app.config("MONGOURL") = os.environ.get("MONGO_URL")

mongo = Pymongo(app)  # create an instance of Pymongo with app object being pushed as argument


@app.route("/")
def test():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=os.getenv("PORT"), 
            debug=True)
