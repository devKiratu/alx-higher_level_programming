#!/usr/bin/python3
"""Test suite for Square class"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    def test_square__str__(self):
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
