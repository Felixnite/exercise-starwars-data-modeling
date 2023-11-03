import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}



class User(Base) :
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email = Column(String(40), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    favorites = relationship('Favorite', backref='user')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    species = Column(String(20))
    gender = Column(String(15))
    eye_color = Column(String(10))
    hair_color = Column(String(10))
    favorites = relationship('Favorite', backref='characters')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    terrain = Column(String(50))
    climate = Column(String(30))
    population = Column(String(20))
    favorites = relationship('Favorite', backref='planets')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
