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

    def test_user_attr_email(self):
        """
        Tests if the email attribute is a string
        """
        inst = User()
        self.assertIsInstance(inst.email, str)

    def test_user_attr_password(self):
        """
        Tests if the password attribute is a string
        """
        inst = User()
        self.assertIsInstance(inst.password, str)

    def test_user_attr_first_name(self):
        """
        Tests if the first_name attribute is a string
        """
        inst = User()
        self.assertIsInstance(inst.first_name, str)

    def test_user_attr_last_name(self):
        """
        Tests if the last_name attribute is a string
        """
        inst = User()
        self.assertIsInstance(inst.last_name, str)
