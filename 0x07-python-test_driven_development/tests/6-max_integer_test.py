#!/usr/bin/python3
"""Unittest for function max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class to test max_integer function
    """
    def test_int_float(self):
        """
        Tests with differente types of inputs
        """
        self.assertEqual(max_integer([1, 2, 3, -14]), 3)
        self.assertEqual(max_integer([1, 2, 3.2, -14.8]), 3.2)
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 1000, float('-inf')]), 1000)

    def test_different_values(self):
        self.assertEqual(max_integer([10, 10, 10, 10]), 10)
        self.assertEqual(max_integer([10.2, 10, 20, -10]), 20)
        self.assertEqual(max_integer([10, -10, 5, 10]), 10)
        self.assertEqual(max_integer([10, 9, 0, 7]), 10)
        self.assertEqual(max_integer([17.8, -20, 16, 80]), 80)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_no_arguments(self):
        self.assertEqual(max_integer(), None)

    def test_string_and_tuple(self):
        self.assertEqual(max_integer("Holberton"), 't')
        self.assertEqual(max_integer((35, 40)), 40)

    def test_array_string_tuples(self):
        self.assertRaises(TypeError, max_integer, ["Holberton", "Hello", 3])
        self.assertEqual(max_integer(("Hello", "World")), "World")
        self.assertRaises(TypeError, max_integer, ("Hello", 21, "World"))
