#!/usr/bin/python3
"""
This module contains class(es) that has shared utility methods
"""
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

time = "%Y-%m-%dT%H:%M:%S.%f"


class Utils:
    """ A Utils class is not to be used as is
    but to be inherited from

    it contains methods like: to_dict, save
    """


    def to_dict(self):
        """ Return a dictionary representation of our object """
        new_dict = self.__dict__.copy()
        if 'created_at' in new_dict:
            new_dict['created_at'] = new_dict['created_at'].strftime(time)
        if 'updated_at' in new_dict:
            new_dict['updated_at'] = new_dict['updated_at'].strftime(time)
        new_dict['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def save(self):
        """ updates the attribute and save the object """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """ delete the current instance of the object from storage """
        models.storage.delete(self)
