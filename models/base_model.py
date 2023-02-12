#!/usr/bin/python3

"""
   Contains class BaseModel
"""

from datetime import datetime
import models
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """The BaseModel class from  which future classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""

        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.utcnow()
                self.updated_at = self.created_at


