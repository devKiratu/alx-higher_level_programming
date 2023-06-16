#!/usr/bin/python3
"""Test suite for Rectangle Class"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for the Rectangle"""
    def test_initialization(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10, 3, 5, 7)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 5)
        self.assertEqual(r2.id, 7)

    def test_invalid_data(self):
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, "2")

        with self.assertRaises(TypeError):
            r3 = Rectangle("10", 2)

        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 5)

        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -2)

        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, "2", 3)

        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 7, 2, "-3")

        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 2, 5, -5)

        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 2, -5, 5)

    def test_area(self):
        r1 = Rectangle(3,2)
        self.assertEqual(r1.area(), 6)
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)
        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)
        r1 = Rectangle(30,22)
        self.assertEqual(r1.area(), 660)
