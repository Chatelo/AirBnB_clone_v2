#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


# class State(BaseModel):
#     """ State class """
#     name = ""
# Import SQLAlchemy and other necessary modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    """This class manages storage of hbnb models using SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine and session to interact with the database"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects depending on the class name"""
        from models import base_model, user, state, city, amenity, place, review
        classes = {
            'BaseModel': base_model.BaseModel,
            'User': user.User,
            'State': state.State,
            'City': city.City,
            'Amenity': amenity.Amenity,
            'Place': place.Place,
            'Review': review.Review
        }
        objects = {}
        if cls:
            query = self.__session.query(classes[cls])
            for obj in query:
                key = "{}.{}".format(cls, obj.id)
                objects[key] = obj
        else:
            for cls_name, cls in classes.items():
                query = self.__session.query(cls)
                for obj in query:
                    key = "{}.{}".format(cls_name, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database session"""
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()


