#!/usr/bin/python3
"""
Modules containig series of tests for a pool object
"""
import unittest
from datetime import datetime
from models.pool import Pool
from models.people.collector import Collector
from models.people.participant import Participant

from models.custom_exceptions import PoolLimitReached


class TestPool(unittest.TestCase):
    """
    Series of test cases for a pool object
    """
    
    def setUp(self):
        """ create a Pool object """
        pool = Pool(name='Diamond Global Savings',
                    collector_id='dddd',
                    amount='300000',
                    rounds=50,
                    mode='payment_day',
                    fee_type='fixed',
                    fee=5000
                    )
        self.pool = pool

    def tearDown(self):
        """ delete a Pool object """
        del self.pool
    
    def test_object_is_a_valid_instance_of_pool_class(self):
        """
        test that a pool object we created is a valid instance of the
        Pool class
        """
        new_pool = Pool(
                name='Mr Promise Group',
                amount=5000,
                rounds=40,
                mode='collect',
                fee_type='percentage',
                fee=0.50
                )
        self.assertIsInstance(new_pool, Pool)

    def test_that_pool_dunder_dict_attribute_is_not_empty(self):
        """ test that Pool has a non-empty dict attribute """
        self.assertIsInstance(self.pool.__dict__, dict)
        self.assertNotEqual(len(self.pool.__dict__), 0)

    def test_pool_to_dict_method(self):
        """ test that the pool object has a to_dict()
        method and it behaves appropraitely """
        self.assertIsInstance(self.pool.to_dict(), dict)
        self.assertIn(self.pool.name, self.pool.to_dict().values())

    def test_util_contains_class_of_object(self):
        """ test that the dictionary returned by the to_dict method
        contains the class of the object """
        self.assertIn(self.pool.__class__.__name__,
                      self.pool.to_dict().values())

    def test_pool_has_required_attributes(self):
        """ test that a pool has all the required attributes """
        self.assertIn('id', self.pool.__dict__)
        self.assertIn('members', self.pool.__dict__)
        self.assertIn('collector_id', self.pool.__dict__)

    def test_pool_recreation_with_dictionary(self):
        """ test to make sure a Pool object can be recreated with
        a dictionary """
        pool_dict = self.pool.to_dict()
        self.assertIsInstance(Pool(pool_dict), Pool)
        self.assertEqual(pool_dict, self.pool.to_dict())
        pool_dict['name'] = 'Super Group'
        self.assertIsInstance(Pool(pool_dict), Pool)
    
    def test_pool_add_memer_method(self):
        """ Test that the add member method properly
        adds a memer to a pool"""
        coll = Collector('Joshua', 'Adeyemi', 'joe@mal.com', 'dpjdkje')
        pool_object = coll.create_pool(
                              pool_name='Harmony Savings Club',
                              amount=2000,
                              start_date=datetime.utcnow(),
                              end_date=datetime.utcnow(),
                              payment_intervals=7,
                              target_number_of_participants=2,
                              mode_of_collection=1,
                              fee_type=1,
                              fee=200,
                              rounds=20
                              )
        new_participant = Participant(lastname='Ajobiewe',
                                      firstname='Joseph',
                                      email='joe@gmail.com',
                                      password='3kjjd93')
        coll.add_member_to_pool(pool_object, new_participant)
        self.assertIn(new_participant.id, pool_object.members)
        new_participant2 = Participant(lastname='Olorunda',
                                      firstname='Hamifue',
                                      email='hamsik@gmail.com',
                                      password='3kjjd93')
        coll.add_member_to_pool(pool_object, new_participant2)
        self.assertIn(new_participant2.id, pool_object.members)
        new_participant3 = Participant(lastname='Daniel',
                                      firstname='Amos',
                                      email='amos@gmail.com',
                                      password='3kjjd93')
        with self.assertRaises(PoolLimitReached):
            coll.add_member_to_pool(pool_object, new_participant3)

    def test_awaiting_approval(self):
        """ Awaiting approval is for when a participant requests
        inclusion into a pool, a request for approval is sent to the 
        collector """
        coll = Collector('Joshua', 'Adeyemi', 'joe@mal.com', 'dpjdkje')
        pool_object = coll.create_pool(
                              pool_name='Harmony Savings Club',
                              amount=2000,
                              start_date=datetime.utcnow(),
                              end_date=datetime.utcnow(),
                              payment_intervals=7,
                              target_number_of_participants=2,
                              mode_of_collection=1,
                              fee_type=1,
                              fee=200,
                              rounds=20
                              )
        new_participant = Participant(lastname='Ajobiewe',
                                      firstname='Joseph',
                                      email='joe@gmail.com',
                                      password='3kjjd93')
        new_participant.join_pool(pool_object)
        self.assertIn(new_participant.id, pool_object.pending_join_requests)
        self.assertIn(new_participant.id, coll.join_requests[pool_object.id])


if __name__ == '__main__':
    unittest.main()
