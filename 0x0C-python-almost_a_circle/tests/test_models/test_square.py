#!/usr/bin/python3
"""Test suite for Square class"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    def test___str__(self):
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s2 = Square(2, 2, 0, 2)
        self.assertEqual(s2.__str__(), "[Square] (2) 2/0 - 2")
        s3 = Square(3, 1, 3, 3)
        self.assertEqual(s3.__str__(), "[Square] (3) 1/3 - 3")

    def test_size(self):
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_update(self):
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 1)
        s1_dict = s1.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1_dict, expected)
        self.assertIsInstance(s1_dict, dict)
