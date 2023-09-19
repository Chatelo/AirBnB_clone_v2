#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


# class City(BaseModel):
#     """ The city class, contains state ID and name """
#     state_id = ""
#     name = ""
# Import SQLAlchemy and other necessary modules
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """The city class, contains state ID and name"""
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Add a relationship with City for DBStorage
    if storage_type == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

