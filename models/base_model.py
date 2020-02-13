#!/usr/bin/python3
# First draft of #3 BaseModel
from uuid import uuid4
from datetime import datetime.now()
Class BaseModel:
    def __init__(self):
        self.id = str(uuid)
        self.created_at = datetime
        self.updated_at = datetime

    def __str__(self):
        c = type(self).__name__
        i = self.id
        d = self.__dict__
        print("[%s] (%s) <%s>".format(c, i, d))

    def save(self):
        self.updated_at = datetime

    def to_dict(self):
        attrs = dict(self.__dict__)
        attrs['__class__'] = type(self).__name__
        attrs['created_at'] = self.created_at.isoformat()
        attrs['updated_at'] = self.updated_at.isoformat()
        return attrs
