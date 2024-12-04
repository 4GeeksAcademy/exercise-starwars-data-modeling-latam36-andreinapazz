import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    signo = Column(String(250), nullable=True)
    foto = Column(String(250), nullable=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

    favorito = relationship("Favorito", back_populates="usuario")


class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    altura = Column(Integer)
    color_ojos = Column(String(250))
    peso = Column(Integer, nullable=False)
    planeta_nacimiento = Column(String(250), nullable=False)

    favorito = relationship("Favorito", back_populates="personaje")
    

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    diametro = Column(Integer)
    gravedad = Column(Integer)
    clima = Column(String(250))
    poblacion = Column(Integer, nullable=False)

    favorito = relationship("Favorito", back_populates="planeta")
    

class Favorito (Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=False)

    usuario = relationship("Usuario", back_populates="favorito")
    personaje = relationship("Personaje", back_populates="favorito")
    planeta = relationship("Planeta", back_populates="favorito")

git 
def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
