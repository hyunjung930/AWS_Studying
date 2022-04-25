from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/movies")
def show_movies():
    return "<h1>Sesac Movies</h1>"