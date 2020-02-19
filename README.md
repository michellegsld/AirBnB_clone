# 0x00 - AirBnB Clone - The Console
#### Repository: AirBnB_clone
#### Project provided by Holberton School NHV

## Description
In this project, students create a command interpreter to manage their AirBnB projects. This is done through a simple flow of th serialization and deserialization processes through instantiation, dictionaries, JSON strings, and files. This results in an organized set of classes used for items such as *USER*, *STATE*, *CITY*, *PLACE*, all inherited from the project's *BaseModel*.
With all of this in mind, the project is given several specifications to follow. The first point to keep in mind is the projects need to work on both interactive and non-interactive mode, with the major difference being in interactive mode, the console reads commands input by the user. 

## Project Directories and Files

#### In **AirBnB_clone** directory:
Names | Descriptions
----- | -------------------
models | Directory containing
tests | Directory containing unittesting for this project
console.py | Python file containing the structure for the console's operations

#### In **models** directory:
Names | Descriptions
----- | -------------------
engine | *Directory* containing file_storage.py
amenity.py | Child class of BaseModel to define HBnB *amenities*
base_model.py | Parent class to define attributes and methods for other classes
city.py |  Child class of BaseModel to define HBnB *cities*
place.py | Child class of BaseModel to define specifications for the HBnB *place* (ie. name, description, # of rooms/bathrooms, guest max, price etc.)
review.py | Child class of BaseModel to define HBnB *review* with place, user and text
state.py | Child class of BaseModel to define HBnB *states*
user.py | Child class of BaseModel to define HBnB *user* with email, password and name

#### In **tests** directory:
Names | Descriptions
----- | -------------------
test_models | *Directory* holds all the following test files
test_engine | *Directory* containing test_file_storage.py
test_amenity.py | Tests for the proper use of amenity specifications
test_base_model.py | Tests for proper use of ParentClass within inheritence
test_city.py | Tests for the proper use of city specifications
test_place.py | Tests for the proper use of place specifications
test_review.py | Tests for the proper use of review specifications
test_state.py | Tests for the proper use of state specifications
test_user.py | Tests for the proper use of user specifications

#### Authors
Written for HolbertonNHV by Michelle Giraldo and Kathleen McKiernan
