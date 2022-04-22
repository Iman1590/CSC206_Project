# Example from https://docs.sqlalchemy.org/en/14/orm/tutorial.html
# Example from https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_related_objects.htm

# import the framwework
from enum import unique
import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine, func
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import sessionmaker, relationship
from db_connector import DbConnector

# Create the application instance
app = Flask(__name__)

# Base class for declaring tables
Base = declarative_base()


class Money(Base):
    __tablename__ = 'Money'
    primary_id = Column(Integer, primary_key=True)
    athlete_name = Column(String, nullable=False)
    amount_paid = Column(Integer, nullable=False)

class Sport(Base):
    __tablename__ = 'Sports'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    sport_played = Column(String(255), nullable=False)

@app.route('/')
def index():

    db = DbConnector()
    session = db.session

    Athletes = session.query(Sport, Money)

    for record in Sport:
        print(record)

    return render_template('form.html', Sport=Sport)

if __name__ == '__main__':
    app.run(debug=True)