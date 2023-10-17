from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Main index.html rendering"""
    return render_template("index.html")
