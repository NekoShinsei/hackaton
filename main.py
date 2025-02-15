from flask import Flask, redirect, render_template, url_for
from flask import request, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return jsonify(error="This path does not exist."), 404

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

app.run("127.0.0.1", 80, debug=True) 