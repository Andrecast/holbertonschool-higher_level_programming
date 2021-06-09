#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import models.base
from models.base import Base
from models.rectangle import Rectangle
import os


class TestClassBase(unittest.TestCase):
    """Test class to test Base class"""
    def test_shebang(self):
        """test for shebang"""
        with open("models/base.py", "r") as file:
            first_line = file.readline()
            self.assertEqual(first_line, "#!/usr/bin/python3")

    def test_pep8(self):
        """testing style"""
        with os.popen("pep8 models/base.py") as file:
            self.assertEqual(file.read(), '')

    def test_doc(self):
        comments_mod = models.base.__doc__
        self.assertTrue(len(comments_mod.splitlines()) > 0)

    def test_Class_doc(self):
        comments_class = models.base.Base.__doc__
        self.assertTrue(len(comments_class.splitlines()) > 0)

    def test_id(self):
        base1 = models.base.Base()
        self.assertEqual(base1.id, 1)

        base2 = models.base.Base(None)
        self.assertEqual(base2.id, 2)

        base3 = models.base.Base(460)
        self.assertEqual(base3.id, 460)

        base4 = models.base.Base()
        self.assertEqual(base4.id, 3)

if __name__ == '__main__':
    unittest.main()
