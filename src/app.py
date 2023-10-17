from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Main index.html rendering"""
    return render_template("index.html")


@app.route("/api/requests/", methods=["GET"])
def hello_world_get():
    """Display a Hello world string"""
    return "<h1>HELLO WORLD!</h1>"
