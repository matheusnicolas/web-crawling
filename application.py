from flask import Flask, render_template, json
import os

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
data = json.load(open(json_url))

@app.route("/numbers", method=['GET'])
def index():
    return render_template("index.html", data=data['numbers'])