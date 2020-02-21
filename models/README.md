# 0x00 - AirBnB Clone - Models
#### Directory: AirBnB_clone/models
#### Project provided by Holberton School NHV

## Description
In this directory, students create project models to define amenities, cities, places, reviews, states and users for the HBnB console.

## Project Directories and Files

#### In **models** directory:
Names | Descriptions
----- | -------------------
engine | *Directory* containing file_storage.py (de/serializes to or from JSON to instances)
amenity.py | Child class of BaseModel to define HBnB *amenities*
base_model.py | Parent class to define attributes and methods for other classes
city.py |  Child class of BaseModel to define HBnB *cities*
place.py | Child class of BaseModel to define specifications for the HBnB *place* (ie. name, description, # of rooms/bathrooms, guest max, price etc.)
review.py | Child class of BaseModel to define HBnB *review* with place, user and text
state.py | Child class of BaseModel to define HBnB *states*
user.py | Child class of BaseModel to define HBnB *user* with email, password and name

#### Authors
Written for HolbertonNHV by Michelle Giraldo and Kathleen McKiernan
