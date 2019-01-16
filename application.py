from flask import Flask, render_template, json, url_for, jsonify
import os

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
data = json.load(open(json_url))

app = Flask(__name__)

@app.route("/numbers")
def index():
    return render_template("index.html", data=data['numbers'])

@app.route("/numbers/json")
def jsonfy():
    return jsonify(data)