# Dinosaur App
# Erin Howell
# Summer 2016
# File for Running the App and Holding the Routes

# import datetime to record time
from datetime import datetime
# import database schema tools (columns, types, time, foreign key (method for
# limiting values specified by one table to those available in another), and
# enum(for set options))
from sqlalchemy import (Column, Integer, String, DateTime, ForeignKey, Enum)
# import declarative base (to use database as code object)
from sqlalchemy.ext.declarative import declarative_base
# import object relational mapper relationship module to link tables
from sqlalchemy.orm import relationship

# Declarative base allows the use of an object to represent the tables, mapper
# and classes of the database
Base = declarative_base()


# Schema
#################
# Date and time table
# takes in an object to record info about
class DateTimeMixin(object):
    # DateTimeMixin has an attribute for when an object was created and for
    # when an object was updated.
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)


# Table to hold information about dinosaurs
# Takes in the database object (???)
class Dinosaur(Base):
    # Class using a declarative needs at least a __tablename__ and a primary
    # key
    __tablename__ = 'Dinosaur'
    name = Column(String(128), nullable=False)
    scientific_name = Column(String(128), nullable=False, unique=True,
                             primary_key=True)
    # Enum type requires a name
    period = Column(Enum('Triassic', 'Jurassic', 'Cretaceous',
                         name='TimePeriod'))

    def __repr__(self):
        # Format string representation of the table ????
        info = 'Dinosaurs<name: {one}, scientific_name: {two} period {three}>'
        formatted = info.format(one=self.name, two=self.scientific_name,
                                three=self.period)

        return formatted
