#!/usr/bin/python3
# First draft of #3 BaseModel
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        fmt = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs is not None and len(kwargs) > 0:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], fmt)
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], fmt)
            (self.__dict__).update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        c = str(type(self).__name__)
        i = str(self.id)
        d = str(self.__dict__)
        return "[" + c + "] " + "(" + i + ") " + d

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        attrs = dict(self.__dict__)
        attrs['__class__'] = type(self).__name__
        attrs['created_at'] = self.created_at.isoformat()
        attrs['updated_at'] = self.updated_at.isoformat()
        return attrs
