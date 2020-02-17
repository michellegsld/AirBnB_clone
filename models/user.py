#!/usr/bin/python3
"""
user.py
User Class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This a child class of BaseModel
    It'll define Users for HBnB
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
