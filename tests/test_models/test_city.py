#!/usr/bin/python3
"""
Unittest for city.py
"""
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.city import City
from uuid import UUID
from datetime import datetime


class TestCity(TestBaseModel):
    """
    A child class of TestBaseModel()
    """

    def __init__(self, *args, **kwargs):
        """
        Calls the parent test class after changing:
        - test_class
        - test_name
        """
        self.test_class = City
        self.test_name = "City"
        super().__init__(*args, **kwargs)
