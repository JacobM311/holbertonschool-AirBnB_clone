#!/usr/bin/python3
""" unit tests for BaseModel class """
import inspect
import models
import pep8
from models import base_model
from models.base_model import BaseModel
import unittest
from datetime import datetime, time

class TestBaseModelDocs(unittest.TestCase):
    """ tests for basemodel """


    @classmethod
    def setUpClass(cls):
        """ setup for doc test """
        cls.base_funcs = inspect.getmembers(BaseModel, inpsect.isfunction)

    def test_ModuleDocstring(self):
        """ tests for docstring """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_FuncDocstrings(self):
        """ tests for docstrings """
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.save.__doc__) >= 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 1)

if __name__ == '__main__':
    unittest.main()
