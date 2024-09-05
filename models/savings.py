#!/usr/bin/python3
"""
This module defines a savings object
"""
import uuid
from datetime import datetime
from models.shared_utils import Base, Utils
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship


class SavingCampaign(Base):
    """ A saving campaign associated with a savings pool """
    __tablename__ = "savings_campaign"
    id = Column(String(60), nullable=False, primary_key=True)
    amount = Column(Integer, nullable=False)
    last_contribution = Column(DateTime, nullable=False)
    participant_id = Column(String(60), ForeignKey('participants.id'),
            nullable=False)
    pool_id = Column(String(60), ForeignKey('pools.id'),
            nullable=False)

    participant = relationship('Participant', backref='saving_campaign')
    pool = relationship('Pool', backref='saving_campaign')


class Saving(Base):
    """
    A class that defines a savings object
    """
    __tablename__ = 'savings'
    id = Column(String(60), nullable=False, primary_key=True)
    payment_date = Column(DateTime, nullable=False)
    amount = Column(Integer, nullable=False)
    campaign_id = Column(String(60), ForeignKey('savings_campaign.id'))


    def __init__(self, amount):
        """ create a savings object """
        self.date = datetime.utcnow()
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.campaign_id = None
