# Dinosaur App
# Erin Howell
# Summer 2016
# File for Running the App and Holding the Routes

# import web development framework
from flask import (Flask)
# import ability to use html templates,...
from flask import (render_template)
# import the database session
import db
# import the database plan
import schema
# import module for python abstract syntax trees which allows code modification
# before compiling (useful for adaptive code)

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
    # pass in origin, Base and engine to create the schemas in the database
    schema.Base.metadata.create_all(db.engine)
    return "Evolved!"


# Mainpage of the site
@app.route('/')
def main():
    return render_template('main.html')


@app.route('/dinoFam')
def dinoFam():
    return render_template('prehistoric.html')

@app.route('/pangea')
def pangea():
    return render_template('pangea.html')






