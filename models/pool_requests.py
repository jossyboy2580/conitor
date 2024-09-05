#!/usr/bin/python3
"""
A pool join request object
"""
import models
from datetime import datetime
from models.pool import Pool
from models.people.participant import Participant
from models.people.collector import Collector
from models.shared_utils import Utils, Base
from sqlalchemy import Column, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class PoolJoinRequest(Utils, Base):
    """
    A pool join REQUEST object
    """
    __tablename__ = 'pool_join_requests'
    id = Column(String(60), primary_key=True)
    participant_id = Column(String(60), ForeignKey("participants.id"),
                            nullable=False)
    pool_id = Column(String(60), ForeignKey("pools.id"),
                     nullable=False)
    status = Column(Enum('approved', 'pending', 'rejected'),
                    default='panding')
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    pool = relationship('Collector', backref='join_requests')
    participant = relationship('Participant', backref='pool_join_requests')

    def approve(self):
        """ Approve a join request """
        if self.status == 'pending':
            self.status = 'approved'
            self.updated_at = datetime.utcnow()
            pool = models.storage.get(Pool, pool_id)
            participant = models.storage.get(Participant, participant_id)
            pool.add_member(participant)
            models.storage.save()
        else:
            raise ValueError('This request has already been approved.')

    def reject(self):
        """ Reject a join request """
        if self.status == 'pending':
            self.status = 'rejected'
            self.updated_at = datetime.utcnow()
            models.storage.save()
        else:
            raise ValueError('This request has already been approved.')
