#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity
from uuid import UUID
from datetime import datetime


class TestAmenity(TestBaseModel):
    """
    A child class of TestBaseModel()
    """

    def __init__(self, *args, **kwargs):
        """
        Calls the parent test class after changing:
        - test_class
        - test_name
        """
        self.test_class = Amenity
        self.test_name = "Amenity"
        super().__init__(*args, **kwargs)
