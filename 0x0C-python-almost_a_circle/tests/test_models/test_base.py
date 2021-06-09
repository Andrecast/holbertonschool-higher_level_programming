#!/usr/bin/python3
"""Unittest for class Base, de los modulos importar solo el metodo necesario
para no usar tantos recursos (pesan más)"""
from unittest import TestCase
import models.base
from models.base import Base
from models.rectangle import Rectangle
import os


class TestClassBase(TestCase):
    """Test class to test Base class"""
    def test_shebang(self):
        """test for shebang"""
        with open("models/base.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_pep8(self):
        """testing style"""
        with os.popen("pep8 models/base.py") as file:
            self.assertEqual(file.read(), '')

    def test_doc(self):
        """test for module documentation"""
        self.assertTrue(len(models.base.__doc__) != 0)

    def test_Class_doc(self):
        """test for class documentation"""
        class_doc = Base.__doc__
        self.assertTrue(len(class_doc.splitlines()) > 0)

    def test_constructor(self):
        """test instanses of class base"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        b6 = Base(-9)
        b7 = Base(0)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, -9)

    def test_json_string(self):
        """test json string"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(type(Base.to_json_string([dictionary])), str)

        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        """test for save to file"""
        empty = None
        self.assertTrue(type(Base.save_to_file(empty)), [])

    def test_from_json_string(self):
        """test from json string"""
        self.assertEqual(Base.from_json_string(None), "[]")
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

if __name__ == '__main__':
    TestCase.main()
