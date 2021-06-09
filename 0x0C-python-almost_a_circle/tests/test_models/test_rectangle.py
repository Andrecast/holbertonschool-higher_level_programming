#!/usr/bin/python3
"""Unittest for class rectangle"""
import os
import unittest
from models.rectangle import Rectangle
import models.rectangle


class TestClassRectangle(unittest.TestCase):
    """Tests class to test Rectangle class """
    def test_shebang(self):
        """ Test for shebang"""
        with open("models/rectangle.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_pep8(self):
        """testing style"""
        with os.popen("pep8 models/rectangle.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_doc(self):
        """test for module documentation """
        self.assertTrue(len(models.rectangle.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(Rectangle.__doc__) != 0)

    def test_functions_doc(self):
        """ Functions with sufficient documentation """
        self.assertTrue(len(Rectangle.area.__doc__) != 0)
        self.assertTrue(len(Rectangle.display.__doc__) != 0)
        self.assertTrue(len(Rectangle.__str__.__doc__) != 0)
        self.assertTrue(len(Rectangle.update.__doc__) != 0)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) != 0)


class TestRectangleCases(unittest.TestCase):
    """ Create a tests for the rectangle class in edge cases """
    def raise_must_be_integer(self):
        """ Expects it to be of type integer """
        msg = " must be an integer"
        try:
            Rectangle(10, "2")
        except TypeError as attr:
            self.assertEqual(attr.__class__.__name__ + msg)
        try:
            Rectangle("l", 6)
        except TypeError as attr:
            self.assertEqual(attr.__class__.__name__ + msg)
        try:
            Rectangle(4, 6, "x")
        except TypeError as attr:
            self.assertEqual(attr.__class__.__name__ + msg)
        try:
            Rectangle(4, 6, 1, "y")
        except TypeError as attr:
            self.assertEqual(attr.__class__.__name__ + msg)


if __name__ == "__main__":
    unittest.main()
