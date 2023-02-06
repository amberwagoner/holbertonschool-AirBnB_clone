#!/usr/bin/python3
""" AirBnB BaseModel """
from datetime import datetime as date
from uuid import uuid4
import models


class BaseModel:
    """ Base Model """
    def __init__(self, *args, **kwargs):
        """ Initialize base model """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = date.now()
        self.updated_at = date.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, date.strptime(value, time_format))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)

    def __str__(self):
        """ Return string representation of BaseModel """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ Update the attribute update_at with current datetime """
        self.updated_at = date.now()

    def to_dict(self):
        """ Returns a dictionary containing all heys/values of __dict__ """
        book = self.__dict__.copy()
        book["created_at"] = self.created_at.isoformat()
        book["updated_at"] = self.updated_at.isoformat()
        book["__class__"] = self.__class__.__name__
        return book
