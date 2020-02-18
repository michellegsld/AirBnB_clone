#!/usr/bin/python3
"""
This file is needed to create a python package
It creates the variable storage which is used to save instances
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
