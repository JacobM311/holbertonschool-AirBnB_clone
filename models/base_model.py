#!/usr/bin/python3
"""base model"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base Model Class"""
    def __init__(self, *args, **kwargs):
        """Base Model __init__ Method"""

        self.id = str(uuid4())
        self.name = name
        self.updated_at = self.created_at = datetime.now()


    def __str__(self):
        """prints string representation of base"""

    return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """saves"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """dictionary"""

        return dict(self.__dict__,
                    __class__=self.__class__.__name__,
                    updated_at=self.updated_at.isoformat(),
                    created_at=self.created_at.isoformat())
