# Dinosaur App
# Erin Howell
# Summer 2016
# File for Running the App and Holding the Routes

# import web development framework
from flask import (Flask)
# import the database session
import db
# import the database plan
import schema


# Initialize the application with flask and set debug
app = Flask(__name__)
app.debug = True
# create session key to protect database
app.secret_key = 'AL12HEGIadkfj/KDF35quierKDNVAdjahf/a43q'


# Routes in the website
########################

# Create all the tables in the database
@app.route('/dinosour')
def prehistoric():
    schema.Base.metadata.create_all(db.engine)
    return "Evolved!"
