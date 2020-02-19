#!/usr/bin/python3
"""
Unittest for state.py
"""
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.state import State
from uuid import UUID
from datetime import datetime


class TestState(TestBaseModel):
    """
    A child class of TestBaseModel()
    """

    def __init__(self, *args, **kwargs):
        """
        Calls the parent test class after changing:
        - test_class
        - test_name
        """
        self.test_class = State
        self.test_name = "State"
        super().__init__(*args, **kwargs)

    def test_state_attr_name(self):
        """
        Tests if the name attribute is a string
        """
        inst = State()
        self.assertIsInstance(inst.name, str)
