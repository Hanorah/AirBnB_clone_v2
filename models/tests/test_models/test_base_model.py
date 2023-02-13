#!/usr/bin/python3

"""Contains all unit tests for the base_model class"""

import unittest
from models.base_model import BaseModel
from io import stringIO
import sys
import datetime

class TestCase(unittest.TestCase):
    """Testing the base class model"""

    def setUp(self):
        """Initializing instance"""

        self.my_model = BaseModel()
        self.my_model.name = "Abdul Shakur"

    def TearDown(self):
        """Removing instance."""

        del self.my_model
    def test_id_type(self):
        """Checks that the id is of type string"""

        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_ids_differ(self):
        """Checks the ids between two instances are different"""
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_name(self):
        """Check that an attribute can be added"""

        self.assertEqual("Abdul Shakur", self.my_model.name)

    def test_a_updated_created_equal(self):
        """Checks that both dates are equal"""

        self.assertEqual(self.my_model.updated_at.year, self.my_model.created_at.year)

    def test_save(self):
        """Checks that after updating the instance; the differ in the updated_at attribute"""

        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at. old_update)