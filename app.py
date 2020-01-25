from flask import Flask, render_template, redirect, request, url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):  # import file where username and password of MongoDB is saved
    import env

app = Flask(__name__)  # create instance of flask

# add configuration to Flask app
MONGO_URI = os.environ["MONGODB_URI"]
app.config["MONGODB_NAME"] = "task_manager"
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)  # create an instance of Pymongo with app object being pushed as argument


'''def mongo_connect(url):  # function to connect to Mongo with url argument passed in
    try:   # start try/except block
        conn = pymongo.MongoClient(url)  # variable to connect to mongo client db
        return conn  # return variable for connection
    except pymongo.errors.ConnectionFailure as e:  # catch error if connection fails
        print("Could not connect to MongoDB: %s") % e  # print error message which has been defined as 'e' alias'''


@app.route("/")
@app.route("/get_tasks")  # new route decorator to redirect to a particular function for the default view of the app
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())  # return everything in the db collection


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=os.getenv("PORT"), 
            debug=True)


# conn = mongo_connect(MONGO_URI)  # calling function with MONGOBDB url