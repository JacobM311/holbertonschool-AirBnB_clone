#!/usr/bin/python3
""" unit tests for BaseModel class """
import models
import pep8
from models import base_model
from models.base_model import BaseModel
import unittest
from datetime import datetime, time


class TestBaseModelDocs(unittest.TestCase):
    """ docstring tests for basemodel """

    def test_ModuleDocstring(self):
        """ tests for docstring """
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_ClassDocstring(self):
        """ tests for docstring """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_FuncDocstrings(self):
        """ tests for docstrings """
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.save.__doc__) >= 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 1)


class TestBaseModel(unittest.TestCase):
    """ tests for basemodel class """
    def test_model(self):
        bm = BaseModel()
        self.assertIsNotNone(bm)

    def test_id(self):
        """ checks that a basemodel object is created """
        bm = BaseModel()
        self.assertIsNotNone(bm.id)
        bm.id = 92
        self.assertEqual(bm.id, 92)

    def test_updated_at(self):
        """ checks object is working """
        bm = BaseModel()
        self.assertIsNotNone(bm.updated_at)
        bm.updated_at = "12:00"
        self.assertEqual(bm.updated_at, "12:00")

    def test_created_at(self):
        """ checks object is working """
        bm = BaseModel()
        self.assertIsNotNone(bm.created_at)
        bm.created_at = "12:00"
        self.assertEqual(bm.created_at, "12:00")

    def test_iso_formats(self):
        bm = BaseModel()
        self.assertTrue(bm.created_at.fromisoformat(str(bm.created_at)))
        self.assertTrue(bm.updated_at.fromisoformat(str(bm.updated_at)))

    def test_datetime(self):
        """ testing created_at, updated_at and datetime objects """
        time1 = datetime.now()
        bm1 = BaseModel()
        time2 = datetime.now()
        self.assertTrue(time1 <= bm1.created_at <= time2)
        time.sleep(1e-4)
        time1 = datetime.now()
        bm2 = BaseModel()
        time2 = datetime.now()
        self.assertTrue(time1 <= bm2.created_at <= time2)
        self.assertEqual(bm1.created_at, bm1.updated_at)
        self.assertEqual(bm2.created_at, bm2.updated_at)
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

if __name__== '__main__':
    unittest.main()
