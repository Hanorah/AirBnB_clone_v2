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
       :param args:
       :param kwargs:
       Inititializes public instance attributes
       """
       if (len(kwargs) ==0):
           self.id = str(uuid.uuid4())
           self.created_at = datetime.now()
           self.updated_at = datetime.now()
