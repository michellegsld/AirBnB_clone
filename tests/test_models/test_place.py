#!/usr/bin/python3
"""
Unittest for place.py
"""
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place
from uuid import UUID
from datetime import datetime


class TestPlace(TestBaseModel):
    """
    A child class of TestBaseModel()
    """

    def __init__(self, *args, **kwargs):
        """
        Calls the parent test class after changing:
        - test_class
        - test_name
        """
        self.test_class = Place
        self.test_name = "Place"
        super().__init__(*args, **kwargs)
