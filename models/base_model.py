#!/usr/bin/python3
"""base model"""


import json


class BaseModel:
    """Base Model Class"""
    def __init__(self, *args, **kwargs):
        """Base Model __init__ Method"""
        if kwargs:
            
        else:
        self.id = str(uuid.uuid4())
        self.created_at =
        self.updated_at =


    def __str__(self):
        """prints string representation of base"""
    return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """saves"""

    def to_dict(self):
        """dictionary"""
