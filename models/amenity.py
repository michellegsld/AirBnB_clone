#!/usr/bin/python3
"""
amenity.py
Amenity Class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This a child class of BaseModel
    It'll define the Amenities for HBnB
    """
    name = ""
