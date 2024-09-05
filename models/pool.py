#!/usr/bin/python3
"""
This module contains the definition of a pool object
"""
from sqlalchemy import Column, String, DateTime, Enum, ForeignKey, Boolean
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from models.custom_exceptions import PoolLimitReached
from models.shared_utils import Utils, Base
from models.people.participant import participant_pools
import uuid
from datetime import datetime


class Pool(Utils, Base):
    """
    A Pool is a group saving object that participants can register
    into
    """
    __tablename__ = 'pools'
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    amount = Column(Integer, nullable=False)
    rounds = Column(Integer)
    collection_mode = Column(Enum('gather', 'payment_days'))
    is_started = Column(Boolean, default=False)
    fee = Column(Integer, nullable=False, default=0)
    collector_id = Column(String(60), ForeignKey('collectors.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    members = relationship('Participant', secondary=participant_pools,
                           back_populates="pools")

    def __init__(self, *args, **kwargs):
        """Initialize a pool object"""
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
            now = datetime.utcnow()
            if kwargs.get('created_at', None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs[created_at], str)
            else:
                self.created_at = now
            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs[updated_at], str)
            else:
                self.updated_at = now
            if not kwargs.get('id'):
                self.id = str(uuid.uuid4())

    def add_member(self, participant):
        """ add a participant to this pool """
        if participant.id in self.members:
            return False
        if len(self.members) >= self.target_number_of_participants:
            raise PoolLimitReached
        self.members[participant.id] = participant
        return True

    def start(self):
        """ start the pool """
        self.is_started = True
