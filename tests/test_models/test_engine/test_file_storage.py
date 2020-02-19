#!/usr/bin/python3
"""
Unittest for file_storage.py
"""
import unittest
from models.engine.file_storage import FileStorage
import os.path


class TestFileStorage(unittest.TestCase):
    """
    Contains multiple tests
    """

    def tearDown(self):
        """
        To remove "file.json" each time
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_to_file(self):
        """
        Tests if an instance was saved to a file
        """
        self.assertFalse(os.path.exists("file.json"))

    def test_is_dict(self):
        """
        Tests that the all method returns a dictionary
        """
        inst = FileStorage()
        self.assertEqual(type(inst.all()), dict)
