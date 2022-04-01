from flask import Flask, render_template, request, session, abort, redirect
from datetime import datetime
import google_api as g_api
import os
import pathlib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/token", methods=['GET', 'POST'])
def google_api():
    token = request.form['id_token']
    g_api(token)
    return 'success'

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