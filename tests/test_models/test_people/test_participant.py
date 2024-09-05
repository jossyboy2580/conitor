#!/usr/bin/python3
"""
Test cases for a participant object
"""
import unittest
from datetime import datetime

from models.people.participant import Participant
from models.people.collector import Collector
from models.people.base_user import BaseUser
from models.pool import Pool

from models.custom_exceptions import InvalidUserDefinition


class TestParticipant(unittest.TestCase):
    """
    A collection of test methods for a participant object
    """

    def setUp(self):
        """ create a participant object """
        self.participant = Participant('Joseph',
                                       'Ajobiewe',
                                       'jose@gmail.com',
                                       'ekjj3kje0'
                                       )

    def tearDown(self):
        """ Delete a participant object """
        del self.participant

    def test_participant_instantiation_not_empty(self):
        """
        test that a participant instance cannot be instantiated without
        parameters
        """
        with self.assertRaises(InvalidUserDefinition) as arexc:
            wrong_collector_instantiation = Participant()

    def test_collector_is_child_of_base_user(self):
        """
        test that a participant object is a descendant of the BaseUser
        class
        """
        self.assertIsInstance(self.participant, BaseUser)

    def test_join_pool(self):
        """ test the join a pool method of the participant """
        collector = Collector('Joshua', 'Adeyemi', 'joe@mal.com', 'dpjdkje')
        pool_object = collector.create_pool(
                              pool_name='Harmony Savings Club',
                              amount=2000,
                              start_date=datetime.utcnow(),
                              end_date=datetime.utcnow(),
                              payment_intervals=7,
                              target_number_of_participants=20,
                              mode_of_collection=1,
                              fee_type=1,
                              fee=200,
                              rounds=20
                              )
        self.participant.join_pool(pool_object)
        self.assertIn(self.participant.id, pool_object.members)

    def test_make_payment(self):
        """ test the make payment """
        pass


if __name__ == '__main__':
    unittest.main()
