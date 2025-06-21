import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Armando Mac Beath", title2="Fiona", url=os.getenv("URL"))


# About us route which returns the about us html page
@app.route('/about')
def about():
    return render_template('aboutUs.html', title="About Us", url=os.getenv("URL"))

# map route which returns the map html page
@app.route('/map')
def map():
    return render_template('map.html', title="Places we've been", url=os.getenv("URL"))