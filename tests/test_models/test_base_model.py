#!/usr/bin/python3
""" Unittests for models/base_model.py """
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing the BaseModel class """
    def test_bm_init(self):
        """ Tests for init """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_dictionary(self):
        """ Tests dict """
        bm = BaseModel()
        book = bm.to_dict()
        self.assertIsInstance(book, dict)
        self.assertIsInstance(book["created_at"], str)
        self.assertIsInstance(book["updated_at"], str)

    def test_save(self):
        """ Tests save """
        bm = BaseModel()
        create = bm.created_at
        update = bm.updated_at
        bm.save()
        self.assertEqual(bm.created_at, create)
        self.assertNotEqual(bm.updated_at, update)

    def test_twobm(self):
        """ Tests if two BaseModels are equal """
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm.id, bm2.id)

if __name__ == "__main__":
    unittest.main()
