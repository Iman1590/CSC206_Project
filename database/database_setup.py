# import the framwework
from enum import unique
import os
import configparser

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# configparser is part of Python and will read configuration setttings in a 
# variety of formats. https://docs.python.org/3/library/configparser.html
# This file is where you would store usernames and passwords AND you DON'T
# upload the config file to GitHub.
config = configparser.ConfigParser()
config.read('settings.conf')

# Engine is the core interface to the database
dbconnect = config["sqlite:///database.db"]["SQLALCHEMY_DATABASE_URI"]
engine = create_engine(dbconnect, echo=True)

# Create a database session, bind to the engine and prepare to use
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Base class for declaring tables
Base = declarative_base()

# Define tables
class Athletes(Base):
    __tablename__ = 'Athletes'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    nationality = Column(String(50))
    current_rank = Column(int(3))
    prev_year_rank = Column(int(3))
    sport = Column(String(50))
    year = Column(int(4))
    earnings = Column(int(20))
 
# Define tables
class Earnings(Base):
    __tablename__ = 'Earnings'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    sport = Column(String(50))
    earnings = Column(int(20)), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
# Create the tables in the database
Base.metadata.create_all(engine)

session.commit()