#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.user import User
from uuid import UUID
from datetime import datetime


class TestUser(TestBaseModel):
    """
    A child class of TestBaseModel()
    """

    def __init__(self, *args, **kwargs):
        """
        Calls the parent test class after changing:
        - test_class
        - test_name
        """
        self.test_class = User
        self.test_name = "User"
        super().__init__(*args, **kwargs)