#!/usr/bin/python3
"""
Unittest for base_model.py
"""
import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Is the parent class
    Contains tests for multiple cases
    """

    def __init__(self, *args, **kwargs):
        """
        To allow this test file to be dynamic
        All the child classes can change:
        - test_class
        - test_name
        To match their class types
        """
        super().__init__(*args, **kwargs)
        self.test_class = BaseModel
        self.test_name = "BaseModel"

    def test_id(self):
        """
        Tests if the id was casted properly
        """
        inst = self.test_class()
        self.assertIsInstance((inst).id, str)

    def test_created_at(self):
        """
        Tests if the object's created_at is of correct type
        """
        inst = self.test_class()
        self.assertIsInstance((inst).created_at, datetime)

    def test_updated_at(self):
        """
        Tests if the object's updated_at is of correct type
        """
        inst = self.test_class()
        self.assertIsInstance((inst).updated_at, datetime)
