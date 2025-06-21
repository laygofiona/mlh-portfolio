import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Armando Mac Beath", title2="Fiona", url=os.getenv("URL"))

# Hobbies route which returns the hobbies html page
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Our Hobbies", url=os.getenv("URL"))


# About us route which returns the about us html page
@app.route('/about')
def about():
    return render_template('aboutUs.html', title="About Us", url=os.getenv("URL"))

@app.route('/work')
def work():
    return render_template('workExperience.html', title="Work Experience", url=os.getenv("URL"))

