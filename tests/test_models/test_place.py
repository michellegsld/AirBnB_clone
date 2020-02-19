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

    def test_place_attr_city_id(self):
        """
        Tests if the city_id attribute is a string
        """
        inst = Place()
        self.assertIsInstance(inst.city_id, str)

    def test_place_attr_user_id(self):
        """
        Tests if the user_id attribute is a string
        """
        inst = Place()
        self.assertIsInstance(inst.user_id, str)

    def test_place_attr_name(self):
        """
        Tests if the name attribute is a string
        """
        inst = Place()
        self.assertIsInstance(inst.name, str)

    def test_place_attr_description(self):
        """
        Tests if the description attribute is a string
        """
        inst = Place()
        self.assertIsInstance(inst.description, str)

    def test_place_attr_number_rooms(self):
        """
        Tests if the number_rooms attribute is a int
        """
        inst = Place()
        self.assertIsInstance(inst.number_rooms, int)

    def test_place_attr_number_bathrooms(self):
        """
        Tests if the number_bathrooms attribute is a int
        """
        inst = Place()
        self.assertIsInstance(inst.number_bathrooms, int)

    def test_place_attr_max_guest(self):
        """
        Tests if the max_guest attribute is a int
        """
        inst = Place()
        self.assertIsInstance(inst.max_guest, int)

    def test_place_attr_price_by_night(self):
        """
        Tests if the price_by_night attribute is a int
        """
        inst = Place()
        self.assertIsInstance(inst.price_by_night, int)

    def test_place_attr_latitude(self):
        """
        Tests if the latitude attribute is a float
        """
        inst = Place()
        self.assertIsInstance(inst.latitude, float)

    def test_place_attr_longitude(self):
        """
        Tests if the longitude attribute is a float
        """
        inst = Place()
        self.assertIsInstance(inst.longitude, float)

    def test_place_attr_amenity_ids(self):
        """
        Tests if the amenity_ids attribute is a list
        """
        inst = Place()
        self.assertIsInstance(inst.amenity_ids, list)
