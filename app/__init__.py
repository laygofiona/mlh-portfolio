import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict
import datetime

load_dotenv()
app = Flask(__name__)


if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                    user=os.getenv("MYSQL_USER"),
                    password=os.getenv("MYSQL_PASSWORD"),
                    host=os.getenv("MYSQL_HOST"),
                    port=3306)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = mydb
        
mydb.connect()
mydb.create_tables([TimelinePost])

print(mydb)




@app.route('/')
def index():
    return render_template('index.html', title="Armando Mac Beath", title2="Fiona", url=os.getenv("URL"))

# Hobbies route which returns the hobbies html page
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Our Hobbies", url=os.getenv("URL"))

#Route for work experience page
@app.route('/work')
def work():
    return render_template('workExperience.html', title="Work Experience", url=os.getenv("URL"))

# About us route which returns the about us html page
@app.route('/about')
def about():
    return render_template('aboutUs.html', title="About Us", url=os.getenv("URL"))

#Route for education page
@app.route('/education')
def education():
    # Create a dictionary with education data for each person
    education_data = {
        "Fiona": [
            {
                "degree": "MYP (Middle Years Programme) Certificate",
                "institution": "International School Suva",
                "dates": "2016 - 2019",
                "description": "Completed Middle School at a school with an International Curriculum.",
                "icon": "fas fa-school"
            },
            {
                "degree": "IB Diploma Program",
                "institution": "International School Suva",
                "dates": "2020 - 2022",
                "description": "Completed the IB (International Baccalaureate) Program with 40 out of 45 points.",
                "icon": "fas fa-school"
            },
            {
                "degree": "B.S. Computer Science with Honors",
                "institution": "Trent University",
                "dates": "2023 - 2027",
                "description": "Currently on Dean's Honour Roll and co-director of university hackathon.",
                "icon": "fas fa-school"
            },
        ],
        "Armando": [
            {
                "degree": "Primary School Diploma",
                "institution": "Andes International School",
                "dates": "2010 - 2016",
                "description": "School with an international curriculum.",
                "icon": "fas fa-school"
            },
            {
                "degree": "Middle School Diploma",
                "institution": "Andes International School",
                "dates": "2016 - 2019",
                "description": "Graduated with honors. ",
                "icon": "fas fa-school"
            },
            {
                "degree": "High School Diploma",
                "institution": "Prepa Tec Campus Puebla",
                "dates": "2018 - 2021",
                "description": "Program of international baccalaureate.",
                "icon": "fas fa-school"
            },
            {
                "degree": "B.S. in Mechatronics Engineering",
                "institution": "Tecnológico de Monterrey, Campus Puebla",
                "dates": "2021 - 2025",
                "description": "Specializing in automation and robotics. Lead programmer for the FRC team.",
                "icon": "fas fa-graduation-cap"
            }
        ]
    }
    # Render the education template with the education data
    return render_template('education.html', education_data=education_data)

# map route which returns the map html page
@app.route('/map')
def map():
    return render_template('map.html', title="Places we've been", url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    try:
        name = request.form['name']
        email = request.form['email']
        content = request.form['content']
        
        if not name or not name.strip():
            return "Invalid name", 400
        if not email or '@' not in email:
            return "Invalid email", 400
        if not content or not content.strip():
            return "Invalid content", 400

        timeline_post = TimelinePost.create(name=name, email=email, content=content)
        
        return model_to_dict(timeline_post), 200

    except KeyError as e:
        return f"Missing required field: {e}", 400
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in 
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_posts():
    query = TimelinePost.delete()
    query.execute()
    return f"Posts deleted successfully", 200

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")