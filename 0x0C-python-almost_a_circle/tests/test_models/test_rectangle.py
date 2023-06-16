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
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)
        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)
        r1 = Rectangle(30, 22)
        self.assertEqual(r1.area(), 660)

    def test___str__(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(4, 5, 0, 1, 18)
        self.assertEqual(r2.__str__(), "[Rectangle] (18) 0/1 - 4/5")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        # test kwargs
        r2 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r2.__str__(), "[Rectangle] (10) 10/10 - 10/10")
        r2.update(height=1)
        self.assertEqual(r2.__str__(), "[Rectangle] (10) 10/10 - 10/1")
        r2.update(width=1, x=2)
        self.assertEqual(r2.__str__(), "[Rectangle] (10) 2/10 - 1/1")
        r2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r2.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r2.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        expected = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, expected)
        self.assertIsInstance(r1_dict, dict)
