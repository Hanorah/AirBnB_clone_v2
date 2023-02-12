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


    def __str__(self):
        """String representation  of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)



    def save(self):
        """Updates the attribute"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all key/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
