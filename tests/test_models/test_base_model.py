#!/usr/bin/python3
""" Unittests for models/base_model.py """
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing the BaseModel class """
    def setUp(self):
        bm = BaseModel()
    
    def test_bm_init(self):
        """ Tests for init """
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertEqual(bm.created_at, bm.updated_at)

    def test_str(self):
        """ Tests to validate string """
        expected_string = "[BaseModel] ({}) {{'id: {}, 'created_at': {}, 'updated_at': {}"}}".format(bm.id, bm.id, bm.created_at, bm.updated_at)
        self.assertEqual(str(bm), expected_string)

    def test_dictionary(self):
        """ Tests dict """
        book = bm.to_dict()
        self.assertIsInstance(book, dict)
        self.assertIsInstance(book["created_at"], str)
        self.assertIsInstance(book["updated_at"], str)

    def test_save(self):
        """ Tests save """
        create = bm.created_at
        update = bm.updated_at
        bm.save()
        self.assertEqual(bm.created_at, create)
        self.assertNotEqual(bm.updated_at, update)

    def test_equaltime(self):
        """ Tests that created_at and updated_at are equal """
        self.assertEqual(bm.created_at, bm.updated_at)

    def test_twobm(self):
        """ Tests if two BaseModels are equal """
        bm2 = BaseModel()
        self.assertEqual(bm.id, bm2.id)


if __name__ == "__main__":
    unittest.main()
