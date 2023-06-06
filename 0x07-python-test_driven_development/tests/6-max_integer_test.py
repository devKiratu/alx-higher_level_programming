#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_valid_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 9, -3, 5]), 9)
        self.assertEqual(max_integer([-1, -9, -3, -5]), -1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([5.1, 5.6, 5.3, 5.9, 5.7]), 5.9)
        self.assertEqual(max_integer((1, 3, 5, 2, 4)), 5)

    def test_exceptions_raised(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

        with self.assertRaises(TypeError):
            max_integer(5)
