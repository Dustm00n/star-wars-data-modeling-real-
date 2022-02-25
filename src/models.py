import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base() 

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    password = Column(String(250))
    email = Column(String(250))

class Perosnajes_Favoritos(Base):
    __tablename__= 'personajes_favoritos'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('personajes.id'))

class Planetas_Favoritos(Base):
    __tablename__ = 'planetas_favoritos'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planetas.id'))

class Naves_Favoritas(Base):
    __tablename__ = 'naves_favoritas'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('naves.id'))

class Especies_Favoritas(Base):
    __tablename__ = 'especies_favoritas'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('especies.id'))

class Vehiculos_Favoritas(Base):
    __tablename__ = 'vehiculos_favoritas'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('vehiculos.id'))


class Perosnajes(Base):
    __tablename__ = 'personajes'
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

    __tablename__ = 'planetas'
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

    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))


class Vehiculos(Base):

    __tablename__='vehiculos'
    id=Column(Integer,primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))

class Especies(Base):

    __tablename__='especies'
    id= Column(Integer,primary_key=True)
    name = Column(String(250))
    designation =  Column(String(250))
    average_height = Column(String(250))
    average_lifespan = Column(String(250))
    hair_colors =  Column(String(250))
    skin_colors =  Column(String(250))
    eye_colors = Column(String(250))
    homeworld =  Column(String(250))
    language = Column(String(250))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')