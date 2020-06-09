import unittest
import pep8
import io
from io import StringIO
import sys
import json
from models.base import Base
from models import square
Square = square.Square


class TestSquare(unittest.TestCase):
    """ Testing the Square class """

    def test_style_base(self):
        """test pep8
        """
        style = pep8.StyleGuide()
        m = style.check_files(["models/square.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    @classmethod
    def test_sq(cls):
        """ define instances """
        Base._Base__nb_objects = 0
        cls.obj0 = Square(10, 6, 4, 17)
        cls.obj1 = Square(8, 5, 4)
        cls.obj2 = Square(5)
        cls.obj3 = Square(4, 6)
        cls.obj4 = Square(10, 5, 6)
        cls.obj5 = Square(10)

    def test_squ1(self):
        """ testing set id """
        self.assertEqual(self.obj0.id, 17)
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 2)
        self.assertEqual(self.obj3.id, 3)

    def test_sqs(self):
        """ testing instance of Square """
        self.assertEqual(self.obj4.id, 4)
        self.assertEqual(self.obj4.size, 10)
        self.assertEqual(self.obj4.x, 5)
        self.assertEqual(self.obj4.y, 6)

    def test_sqarg(self):
        """ Testing arguments empty, string """
        with self.assertRaises(TypeError):
            dummy = Square()
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            dumy = Square("Nasser", 17)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            dumy = Square(23, "Nasser")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            dumy = Square(23, 5, "Nasser")

    def test_sqarg2(self):
        """ testing negatives arguments"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            dumy = Square(-6, 17)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            dumy = Square(6, -4, 6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            dumy = Square(6, 4, -6,)

    def test_sq4(self):
        """ testing area method """
        self.assertEqual(self.obj5.area(), 100)

    def test_disp(self):
        """ display method """
        obj6 = Square(4)
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        obj6.display()
        self.assertEqual(sys.stdout.getvalue(), "####\n####\n####\n####\n")

    def test_upd(self):
        """ testing update and str method """
        obj10 = Square(17, 17, 17, 17)
        self.assertEqual(str(obj10), "[Square] (17) 17/17 - 17")
        obj10.update(23, 7, 5, 4)
        self.assertEqual(str(obj10), "[Square] (23) 5/4 - 7")
        obj10.update(15)
        self.assertEqual(str(obj10), "[Square] (15) 5/4 - 7")
        obj10.update(16, 10, 8)
        self.assertEqual(str(obj10), "[Square] (16) 8/4 - 10")

    def test_upd_emp(self):
        """ testing empty arguments """
        obj11 = Square(17, 17, 17, 17)
        obj11.update()
        self.assertEqual(str(obj11), "[Square] (17) 17/17 - 17")

    def test_upd_ka(self):
        """ testing **kwargs """
        obj12 = Square(17, 17, 17, 17)
        self.assertEqual(str(obj12), "[Square] (17) 17/17 - 17")
        obj12.update(size=10, x=3, y=2, id=11)
        self.assertEqual(str(obj12), "[Square] (11) 3/2 - 10")
        obj12.update(size=12)
        self.assertEqual(str(obj12), "[Square] (11) 3/2 - 12")
        obj12.update(hola=12)
        self.assertEqual(str(obj12), "[Square] (11) 3/2 - 12")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            obj12.update(size="Nasser")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            obj12.update(x=-1)

    def test_dict(self):
        """ testing to_dictionary method """
        obj13 = Square(12, 6, 5, 33)
        dict13 = obj13.to_dictionary()
        self.assertEqual(dict13, {'id': 33, 'size': 12, 'x': 6, 'y': 5})

    def test_stf01(self):
        """ testing save_to_file method """
        obj13 = Square(17, 17, 17, 22)
        obj14 = Square(17, 17, 17, 20)
        list1 = [obj13, obj14]
        Square.save_to_file(list1)
        with open("Square.json", 'r') as f:
            list2 = [obj13.to_dictionary(), obj14.to_dictionary()]
            self.assertEqual(json.dumps(list2), f.read())

    def test_stf02(self):
        """ testing save_to_file method with None argument """
        Square.save_to_file(None)
        with open("Square.json", 'r') as f:
            self.assertEqual("[]", f.read())

    def test_stf2(self):
        """ testing save_to_file method with empty list """
        list1 = []
        Square.save_to_file(list1)
        with open("Square.json", 'r') as f:
            self.assertEqual(json.dumps(list1), f.read())

    def test_create(self):
        """ testing create method """
        dict4 = {'id': 33, 'size': 12, 'x': 5, 'y': 4}
        obj15 = Square.create(**dict4)
        self.assertEqual(str(obj15), "[Square] (33) 5/4 - 12")
