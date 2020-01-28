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


@app.route("/")
@app.route("/get_tasks")  # new route decorator to redirect to a particular function for the default view of the app
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())  # return everything in the db collection


@app.route("/add_task")
def add_task():
    return render_template("add_task.html", categories=mongo.db.categories.find())  # fetching categories collection to show in option dropdown menu


@app.route("/insert_task", methods=["POST"])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())  # insert the result of the POST request from submitted form and convert it to dictionary format
    return redirect(url_for("get_tasks"))  # once new doc recorded, send back webpage to get_task function


@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editask.html', task=the_task,
                           categories=all_categories)


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")), 
            debug=True)