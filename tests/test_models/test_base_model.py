#!/usr/bin/python3
""" Unittests for models/base_model.py """
import unittest
import uuid
from datetime import datetime as date
import models.base_model
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing the BaseModel class """

    def setUp(self):
        bm = BaseModel()

    def test_basemodel_initializing(self):
        """ Tests for init """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, date)
        self.assertIsInstance(bm.updated_at, date)

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

    def test_two_basemodel(self):
        """ Tests if two BaseModels are equal """
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm.id, bm2.id)

    def test_kwargs(self):
        """ Test initialization with kwargs """
        create = '2023-04-20T00:00:00.000000'
        update = '2023-04-20T00:00:00.000000'
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel(id="69", created_at=create, updated_at=update)
        self.assertEqual(bm.id, "69")
        self.assertEqual(bm.created_at, date.strptime(create, time_format))
        self.assertEqual(bm.updated_at, date.strptime(create, time_format))

    def test_kwargs_none(self):
        """ Tests if None is present in kwargs """
        with self.assertRaises(TypeError):
            bm = BaseModel(id=None,
                          created_at=None,
                          updated_at=None,
                          name=None)
            self.assertTrue(hasattr(bm, "id"))
            self.assertTrue(hasattr(bm, "created_at"))
            self.assertTrue(hasattr(bm, "updated_at"))
            self.assertTrue(hasattr(bm, "name"))   


if __name__ == '__main__':
    unittest.main()
