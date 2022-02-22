import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    password = Column(String(250))
    email = Column(String(250))


  class Perosnajes_Favoritos(Base):
    __tablename__= 'Personajes_Favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))



  class Planetas_Favoritos(Base):
    __tablename__ = 'Planetas_Favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
      id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))



  class Naves_Favoritas(Base):
    __tablename__ = 'Naves_Favoritas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('ships.id'))

  class Especies_Favoritas(Base):
    __tablename__ = 'Especies_Favoritas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('ships.id'))

  class Perosnajes(Base):
    __tablename__ = 'Personajes'
     # Here we define Columns for the table address.
    # Notice that each Column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    skin_color = Column(String(250))


  class Planetas(Base):
    __tablename__ = 'Planetas'
     # Here we define Columns for the table address.
    # Notice that each Column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))

  class Naves(Base):
    __tablename__ = 'Naves'
     # Here we define Columns for the table address.
    # Notice that each Column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))


  class Vehiculos(Base):
    __tablename__='Vehiculos'
    id=column(Integer,primary_key=True)
     name = Column(String(250))
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))

  class Especies(Base):
    __tablename__='Especies'
    id= column(Integer,primary_key=True)
    name = Column(String(250))
    designation =  Column(String(250))
    average_height = Column(String(250))
    average_lifespan = Column(String(250))
    hair_colors =  Column(String(250))
    skin_colors =  Column(String(250))
    eye_colors = Column(String(250))
    homeworld =  Column(String(250))
    language = Column(String(250))







    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')