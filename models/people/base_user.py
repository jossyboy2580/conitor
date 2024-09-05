#!/usr/bin/python3
"""
This module defines a base_user object

A BaseUser is the smallest representation of a
user on Conitor be it a Collector or a Participant
"""
import uuid
from datetime import datetime
from ..custom_exceptions import InvalidUserDefinition
from models.shared_utils import Utils, Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String


class BaseUser:
    """
    A class that defines a base user
    """
    id = Column(String(128), nullable=False, primary_key=True)
    firstname = Column(String(128), nullable=False)
    lastname = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self, *argz, **kwargz):
        """ Initialize a user """
        if kwargz:
            expected_keys = ['lastname','firstname','email','password']
            if sorted(expected_keys) != sorted(kwargz.keys()):
                raise InvalidUserDefinition
            for attr, val in kwargz.items():
                setattr(self, attr, val)
            if kwargz.get('created_at', None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargz[created_at], str)
            else:
                self.created_at = datetime.utcnow()
            if kwargz.get('updated_at', None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargz[updated_at], str)
            else:
                self.updated_at = datetime.utcnow()
            if not kwargz.get('id'):
                self.id = str(uuid.uuid4())
        elif argz:
            if len(argz) < 4:
                raise InvalidUserDefinition
            else:
                self.firstname, self.lastname = argz[0], argz[1]
                self.email, self.password = argz[2], argz[3]
                time = datetime.utcnow()
                self.created_at, self.updated_at = time, time
                self.id = str(uuid.uuid4())
        else:
            raise InvalidUserDefinition

