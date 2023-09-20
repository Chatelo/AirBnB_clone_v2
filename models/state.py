#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'  # Add the table name

    name = Column(String(128), nullable=False)

    # For DBStorage: Define a relationship with City, and cascade delete
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
