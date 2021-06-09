#!/usr/bin/python3
"""Unittest for class Square"""
from models.square import Square
import models.square
import json
import os
import unittest


class TestClassSquare(unittest.TestCase):
    """Test class to test Square class"""
    def test_shebang(self):
        """test for shebang"""
        with open("models/square.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_pep8(self):
        """testing style"""
        with os.popen("pep8 models/square.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.square.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        class_doc = Square.__doc__
        self.assertTrue(len(class_doc.splitlines()) > 0)

    def test_functions_doc(self):
        """ Functions with sufficient documentation """
        self.assertTrue(len(Square.__str__.__doc__) != 0)
        self.assertTrue(len(Square.update.__doc__) != 0)
        self.assertTrue(len(Square.to_dictionary.__doc__) != 0)


if __name__ == "__main__":
    unittest.main()
