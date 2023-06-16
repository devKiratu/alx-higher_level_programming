#!/usr/bin/python3
"""Test class for base.py"""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """defines tests for Base class"""
    def test_ids(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        json_str = Base.to_json_string([r1_dict])
        expected = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]
        self.assertEqual(json_str, json.dumps(expected))
        self.assertIsInstance(json_str, str)
