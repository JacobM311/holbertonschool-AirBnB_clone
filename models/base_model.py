#!/usr/bin/python3
"""base model"""


import json
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base Model Class"""

    def __init__(self, *args, **kwargs):
        """Base Model __init__ Method"""
<<<<<<< HEAD

=======
>>>>>>> b5b332daa2be1650e51b687ba8d6efcaa4d8b1c2
        self.id = str(uuid4())
        self.name = name
        self.updated_at = self.created_at = datetime.now()

    def __str__(self):
        """prints string representation of base"""
<<<<<<< HEAD

    return "[{}] ({}) {}".format(self.__class__.__name__,
                                 self.id, self.__dict__)
=======
        return "[{}] ({}) {}".format(self.__class__.__name__,
<<<<<<< HEAD
                                self.id, self.__dict__)
>>>>>>> b5b332daa2be1650e51b687ba8d6efcaa4d8b1c2
=======
                                     self.id, self.__dict__)
>>>>>>> 8b4165f40e2d0f4cbae82ba5c06a1bfbab5b5ff5

    def save(self):
        """saves"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dictionary"""
        return dict(self.__dict__,
                    __class__=self.__class__.__name__,
                    updated_at=self.updated_at.isoformat(),
                    created_at=self.created_at.isoformat())
