#!/usr/bin/python3
"""
   A BaseModel class that contains all attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
   """
      Base class for all other classes to use
   """
   def __init__(self, *args, **kwargs):
       """
       Initializes the public instance attributes
       :param args:
       :param kwargs:
       """
       if (len(kwargs) ==0):
           self.id = str(uuid.uuid4())
           self.created_at = datetime.now()
           self.updated_at = datetime.now()
           models.storage.new(self)
       else:
           kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                    "%Y-%m-%dT%H:%M:%S.%f")
           kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                    "%Y-%m-%dT%H:%M:%S.%f")

           for key, value in kwargs.items():
               if "__class__" not in key:
                   setattr(self, key, value)

        def __str__(self):
            """
            Returns string representation of BaseModel class
            :param self:
            :return:
            """
            return ("[{}] ({}) {}".format(self.__class__.__name__,
                                          self.id, self.__dict__))


        def __repr__(self):
            """
            Returns string representation of BaseModel class
            :param self:
            :return:
            """

            return("[{}] ({}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__))

        def save(self):
            """
            Update the updated_at attribute
            :param self:
            :return:
            """
            self.updated_at = datetime.now()
            models.storage.save()


        def to_dict(self):
            """
            Returns a dictionary representation of BaseModels class
            :param self:
            :return:
            """
            cp_dict = dict(self.__dict__)
            cp_dict['__class__'] = self.__class__.__name__
            cp_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
            cp_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

            return (cp_dict)


