#!/usr/bin/python3
"""
review.py
Review Class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This a child class of BaseModel
    It'll be a review for HBnB
    """
    place_id = ""
    user_id = ""
    text = ""
