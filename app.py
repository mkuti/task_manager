from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def test():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=os.getenv("PORT"), 
            debug=True)