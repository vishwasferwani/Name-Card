from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def namecard():
    return render_template("index.html")

