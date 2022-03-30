from flask import Flask, render_template, request, session, abort, redirect
from datetime import datetime
import os
import pathlib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/docs")
def docs():
    return render_template('docs.html')

@app.route("/server_time")
def get_server_time():
    return f"Server Time {datetime.now()}"

app.run(debug=True)