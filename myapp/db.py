# Dinosaur App
# Erin Howell
# Summer 2016
# File for Creating the Database and Sessions

# import ORM to coordinate between database and program
import sqlalchemy
# import the module for creating sessions (interaction between program, client,
# and server)
from sqlalchemy.orm import sessionmaker
# import the database configurer
from config import app_config
# import the declarative base module *

# import the database, the debug status *, and create the engine *
db_url = app_config['database']['url']
debug = app_config.getboolean('app', 'debug')
engine = sqlalchemy.create_engine(db_url, echo=debug)


# create a session using the database engine *
def get_session():
    Session = sessionmaker(bind=engine)
    return Session
