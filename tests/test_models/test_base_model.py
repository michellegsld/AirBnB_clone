#!/usr/bin/python3
"""
Unittest for base_model.py
"""
import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime
import os.path


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

    def tearDown(self):
        """
        To remove "file.json" each time
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_class_type(self):
        """
        Tests what the class type of an instance is
        """
        inst = self.test_class()
        self.assertIsInstance(inst, self.test_class)

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

    def test_str(self):
        """
        Tests if the object's __str__ is of correct type
        """
        inst = self.test_class()
        self.assertIsInstance(str(inst), str)

    def test_to_dict(self):
        """
        Tests if the object's to_dict() is of correct type
        """
        inst = self.test_class()
        self.assertIsInstance(inst.to_dict(), dict)

    def test_save(self):
        """
        Tests if the object's save() works correctly
        """
        inst = self.test_class()
        inst.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_kwargs(self):
        """
        Tests if the object's instantiation with kwargs works correctly
        """
        inst1 = self.test_class()
        inst2 = self.test_class(inst1.to_dict())
        self.assertTrue(inst1.created_at, inst2.created_at)
