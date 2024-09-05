#!/usr/bin/python3
"""
This module defines a participant object
"""
from models.people.base_user import BaseUser
from models.shared_utils import Base, Utils
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


participant_pools = Table(
        'participant_pool',
        Base.metadata,
        Column('participant_id', String(60), ForeignKey('participants.id')),
        Column('pool_id', String(60), ForeignKey('pools.id'))
        )

class Participant(BaseUser, Utils, Base):
    """
    This class defines a participant
    """
    __tablename__ = 'participants'
    pools = relationship('Pool', secondary=participant_pools,
                         back_populates='members')

    def __init__(self, *args, **kwargs):
        """ Create a participant instance """
        super().__init__(*args, **kwargs)
        self.registered_pools = []

    def send_join_request(self, pool_object):
        """ apply to join a pool """
        # create a request object and do the recommended according to claude
        from models.pool_requests import PoolJoinRequest
        request = PoolJoinRequest(pool_id=pool_object.id,
                                  participant_id = self.id,
                )
        request.save()
