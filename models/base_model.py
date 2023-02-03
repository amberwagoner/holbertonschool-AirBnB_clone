#!/usr/bin/python3
""" AirBnB BaseModel """
import uuid
import datetime

class BaseModel:
    """ Base Model """
    def __init__(self) -> None:
        pass

    def id(self):
        """ Assign string with an uuid """
        uuid.uuid4()
        str(uuid.uuid4())
        uuid.uuid4().hex

    def created_at(self):
        """ Assign with current datetime """
        now = datetime.datetime.now()

    def updated_at(self):
        """ Update with current datetime """
        now = datetime.datetime.now()
        self.last_accessed = datetime.now()
