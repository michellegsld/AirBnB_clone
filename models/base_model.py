#!/usr/bin/python3
"""
base_model.py
BaseModel Class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This is the Parent class.
    It'll define all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Takes in either args, kwargs, or neither
        - args: Will not be used.
        - kwargs: The dictionary of attributes to create the instance with
            |-> Adds each key, value pair except for __class__
            |-> Converts created_at and updated_at into datetime objects
        If neither were sent in, then a new instance is created with:
        - self.id -> String. Assigned with uuid4()
        - self.created_at -> Datetime. Assigned with datetime.now()
        - self.updated_at -> Datetime. Assigned with datetime.now()
        -> Which is then stored in storage
        """
        from models import storage
        fmt = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs is not None and len(kwargs) > 0:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], fmt)
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], fmt)
            (self.__dict__).update(kwargs)
            if '__class__' in self.__dict__:
                del self.__dict__['__class__']
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Prints the instance as a string using:
        c -> The class name
        i -> The instance's id
        d -> The instance's dictionary of attributes
        """
        c = str(type(self).__name__)
        i = str(self.id)
        d = str(self.__dict__)
        return "[" + c + "] " + "(" + i + ") " + d

    def save(self):
        """
        Sets updated_at to the current datetime
        Saves the changes done to the instance in storage
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary, which contains everything within __dict__
        It also:
        - Adds the __class__ attribute
        - Turns the datetime objects created_at and updated_at into strings.
        """
        attrs = dict(self.__dict__)
        attrs['__class__'] = type(self).__name__
        attrs['created_at'] = self.created_at.isoformat()
        attrs['updated_at'] = self.updated_at.isoformat()
        return attrs
