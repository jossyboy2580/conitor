#!/usr/bin/python3
"""
This module defines a collector object
"""
import models
from models.people.base_user import BaseUser
from models.pool import Pool
from models.shared_utils import Utils, Base

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Collector(BaseUser, Utils, Base):
    """
    This class defines a collector
    """
    __tablename__ = 'collectors'
    pools = relationship('Pool', backref='collector')

    def __init__(self, *args, **kwargs):
        """ Create a collector instance """
        super().__init__(*args, **kwargs)

    def create_pool(self, **data):
        """ Create a new Pool """
        try:
            new_pool = Pool(collector_id= self.id, **data)
        except Exception as exc:
            raise exc
        else:
            new_pool.save()

    def add_member_to_pool(self, pool_object, participant):
        """ add member to a group """
        if pool_object.id not in self.pools:
            return False
        return pool_object.add_member(participant)

    def start_pool(self, pool_object):
        """ Kick start the pool """
        if pool_object.id not in self.pools:
            return
        pool_object.start()
        models.storage.save()
