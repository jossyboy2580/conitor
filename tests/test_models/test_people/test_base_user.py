#!/usr/bin/python3
"""
Testing the base user
"""
import unittest
from models.people.base_user import BaseUser
from models.custom_exceptions import InvalidUserDefinition


class TestBaseUser(unittest.TestCase):
    """ A serires of test cases that are checked """

    def setUp(self):
        """ Test fixture to setup a base user """
        self.base_user = BaseUser(lastname='Adeyanju',
                                  firstname='Victor',
                                  email='pol@me.com',
                                  password='23fq54?;')

    def tearDown(self):
        """ test fixture to destroy a base user """
        del self.base_user

    def test_base_user_type(self):
        """ Test if the bu object is an instance of the BaseUser class """
        self.assertIsInstance(self.base_user, BaseUser)
        self.assertIs(self.base_user.__class__, BaseUser)

    def test_base_user_has_attributes(self):
        """
        Tests to confirm if the base user has the
        required attributes
        """
        # Required(Neccesary) attributes
        self.assertIsNotNone(self.base_user.__dict__.get('lastname'))
        self.assertIsNotNone(self.base_user.__dict__.get('firstname'))
        self.assertIsNotNone(self.base_user.__dict__.get('email'))
        self.assertIsNotNone(self.base_user.__dict__.get('password'))
        self.assertIsNotNone(self.base_user.__dict__.get('created_at'))
        self.assertIsNotNone(self.base_user.__dict__.get('updated_at'))
        self.assertIsNotNone(self.base_user.__dict__.get('id'))

        # Unrequired(bogus) attributes
        self.assertIsNone(self.base_user.__dict__.get('meme'))
        self.assertIsNone(self.base_user.__dict__.get('sinud'))

    def test_invalid_user_definition(self):
        """
        Tests if an attempt to define a user using an invalid definition
        triggers the appropraite exception
        """
        with self.assertRaises(InvalidUserDefinition) as asr:
            # Empty calling of constructor not allowed
            wrong_user_def_1 = BaseUser()
        with self.assertRaises(InvalidUserDefinition) as asr:
            # Non Key-Valued pair with less than items not allowed
            # required = <firstname> <lastname> <email> <password>
            wrong_user_def_1 = BaseUser(
                                        'fisrtname',
                                        'lastname',
                                        'email')
        with self.assertRaises(InvalidUserDefinition) as asr:
            # Key word argument definition without firstname
            wrong_user_def_1 = BaseUser(
                                        lastname='Dumelo',
                                        email='john@movie.com',
                                        password='pdfdj33')
        with self.assertRaises(InvalidUserDefinition) as asr:
            # Key word argument definition without lastname
            wrong_user_def_1 = BaseUser(
                                        firstname='Dumelo',
                                        email='john@movie.com',
                                        password='pdfdj33')
        with self.assertRaises(InvalidUserDefinition) as asr:
            # Key word argument definition without email
            wrong_user_def_1 = BaseUser(
                                        lastname='Dumelo',
                                        firstname='John',
                                        password='pdfdj33')
        with self.assertRaises(InvalidUserDefinition) as asr:
            # Key word argument definition without password
            wrong_user_def_1 = BaseUser(
                                        lastname='Dumelo',
                                        fistname='Jogn',
                                        email='john@movie.com',
                                        )


if __name__ == '__main__':
    unittest.main()
