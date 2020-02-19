#!/usr/bin/python3
"""
Unittest for review.py
"""
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review
from uuid import UUID
from datetime import datetime


class TestReview(TestBaseModel):
    """
    A child class of TestBaseModel()
    """

    def __init__(self, *args, **kwargs):
        """
        Calls the parent test class after changing:
        - test_class
        - test_name
        """
        self.test_class = Review
        self.test_name = "Review"
        super().__init__(*args, **kwargs)

    def test_review_attr_place_id(self):
        """
        Tests if the place_id attribute is a string
        """
        inst = Review()
        self.assertIsInstance(inst.place_id, str)

    def test_review_attr_user_id(self):
        """
        Tests if the user_id attribute is a string
        """
        inst = Review()
        self.assertIsInstance(inst.user_id, str)

    def test_review_attr_text(self):
        """
        Tests if the text attribute is a string
        """
        inst = Review()
        self.assertIsInstance(inst.text, str)
