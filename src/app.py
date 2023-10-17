from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Main index.html"""
    return render_template("index.html")


@app.route("/api/requests/", methods=["GET"])
def get_requests():
    """Get example"""
    return "Lot's of data"
