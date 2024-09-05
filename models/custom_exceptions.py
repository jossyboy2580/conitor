#!/usr/bin/python3
"""
This module contains definitions of custom exceptions
specific to this conitor project

Its purpose is to remove ambiguity and enhance Understanding
of what each error state represents
"""


class InvalidUserDefinition(Exception):
    """ Whenever a user is defined without the proper
    arguments, this exception will be raised """

    def __init__(self,
                 message='Provide a lastname, firstname, email and password'):
        """ Initialization for this exception class """
        self.message = message
        super().__init__(self.message)


class PoolLimitReached(Exception):
    """ Error to be raised when a pool limit has been reached so
    no new member can be added """

    def __init__(self,
                 message='Maximum number of allowed members reached!'):
        """ Initialization for this exception class """
        self.message = message
        super().__init__(self.message)
