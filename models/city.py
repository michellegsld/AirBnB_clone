#!/usr/bin/python3
"""
city.py
City Class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This a child class of BaseModel
    It'll define Cities for HBnB
    """
    state_id = ""
    name = ""
