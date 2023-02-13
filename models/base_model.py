#!/usr/bin/python3

"""
   Contains class BaseModel
"""

import uuid
from datetime import datetime


class BaseModel:
    """Parent class for all other classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """Initialization of public instance attributes"""

        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

            for k, v in kwargs.items():
                if "__class__" not in k:
                    setattr(self, k, v)

    
    def __str__(self):
        """Returns a string representation of BaseModel class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))