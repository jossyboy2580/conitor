#!/usr/bin/python3
"""
Test the various functionalities present in the Collector class
"""
import unittest
from datetime import datetime
from models.people.collector import Collector
from models.people.participant import Participant
from models.people.base_user import BaseUser

from models.custom_exceptions import InvalidUserDefinition

from models.pool import Pool


class TestCollector(unittest.TestCase):
    """
    A collection of tests for the Collector class
    """
    
    def setUp(self):
        """
        create a collector object
        """
        self.coll = Collector('Joshua', 'Adeyemi', 'joe@mal.com', 'dpjdkje')

    def tearDown(self):
        """ Delete the collector object """
        del self.coll

    def test_collector_instantiation_not_empty(self):
        """
        test that a collector instance cannot be instantiated without
        parameters
        """
        with self.assertRaises(InvalidUserDefinition) as arexc:
            wrong_collector_instantiation = Collector()

    def test_collector_is_child_of_base_user(self):
        """
        test that a collector object is a descendant of the BaseUser
        class
        """
        self.assertIsInstance(self.coll, BaseUser)
        self.assertEqual(self.coll.__class__.__base__, BaseUser)

    def test_collector_create_pool_function(self):
        """
        test that a collector object has a created pools attribute
        """
        pool_object = self.coll.create_pool(
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
        self.assertIsInstance(pool_object, Pool)
        self.assertEqual(self.coll.id, pool_object.collector_id)

    def test_that_created_pool_is_in_collectors_pools(self):
        """ test that a pool created by a collector is added
        to the collector's """

    def test_add_member_to_pool(self):
        """ test the add member to pool functionality """
        pool_object = self.coll.create_pool(
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
        self.assertIsInstance(pool_object, Pool)
        new_participant = Participant(lastname='Ajobiewe',
                                      firstname='Joseph',
                                      email='joe@gmail.com',
                                      password='3kjjd93')
        self.coll.add_member_to_pool(pool_object, new_participant)
        self.assertIn(new_participant.id, pool_object.members)
        new_participant2 = Participant(lastname='Olorunda',
                                      firstname='Hamifue',
                                      email='hamsik@gmail.com',
                                      password='3kjjd93')
        self.coll.add_member_to_pool(pool_object, new_participant2)
        self.assertIn(new_participant2.id, pool_object.members)
        new_participant3 = Participant(lastname='Samuel',
                                      firstname='Jong',
                                      email='joe@gmail.com',
                                      password='3kjjd93')
        self.coll.add_member_to_pool(pool_object, new_participant3)
        self.assertIn(new_participant3.id, pool_object.members)
        # Assert the new length of the dict
        self.assertEqual(3, len(pool_object.members))
        # confirm that the collector own the pool
        self.assertEqual(self.coll.id, pool_object.collector_id)

    def test_start_pool_method(self):
        """ test that a pool has been started """
        pool_object = self.coll.create_pool(
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
        self.assertIs(pool_object.is_started, False)
        self.coll.start_pool(pool_object)
        self.assertIs(pool_object.is_started, True)

    def test_approve_member_payment(self):
        """ test that the method to approve payment works """
        pool_object = self.coll.create_pool(
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
        self.assertIsInstance(pool_object, Pool)
        new_participant = Participant(lastname='Ajobiewe',
                                      firstname='Joseph',
                                      email='joe@gmail.com',
                                      password='3kjjd93')
        # check_for pool join requests
        # approve them if the group is not full


if __name__ == '__main__':
    unittest.main()
