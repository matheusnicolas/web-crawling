from flask import Flask, render_template, json, url_for
import os

app = Flask(__name__)

@app.route("/numbers")
def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
    data = json.load(open(json_url))
    return render_template("index.html", data=data['numbers'])