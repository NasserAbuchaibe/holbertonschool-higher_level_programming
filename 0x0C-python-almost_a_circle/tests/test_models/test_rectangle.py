import unittest
import pep8
import io
from io import StringIO
import sys
import json
from models.base import Base
from models import rectangle
Rectangle = rectangle.Rectangle


class Test_Rectangle(unittest.TestCase):
    """ Testing the Rectangle class """

    def test_style_rectangle(self):
        """test pep8
        """
        style = pep8.StyleGuide()
        m = style.check_files(["models/base.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    @classmethod
    def test_rectangle(cls):
        """ define instances """
        Base._Base__nb_objects = 0
        cls.obj = Rectangle(10, 6, 0, 0)
        cls.obj1 = Rectangle(10, 5, 4, 4)
        cls.obj2 = Rectangle(8, 4, 2, 1)
        cls.obj3 = Rectangle(6, 3)
        cls.obj4 = Rectangle(10, 6, 0, 0, 23)
        cls.obj5 = Rectangle(10, 6, 0, 0)
        cls.obj6 = Rectangle(7, 4)
        cls.obj8 = Rectangle(10, 4)

    def test_rectangle_id(self):
        """ testing set id """
        self.assertEqual(self.obj.id, 1)
        self.assertEqual(self.obj1.id, 2)
        self.assertEqual(self.obj2.id, 3)
        self.assertEqual(self.obj3.id, 4)
        self.assertEqual(self.obj4.id, 23)

    def test_s(self):
        """ testing instances """
        self.assertEqual(self.obj5.id, 5)
        self.assertEqual(self.obj5.width, 10)
        self.assertEqual(self.obj5.height, 6)
        self.assertEqual(self.obj5.x, 0)
        self.assertEqual(self.obj5.y, 0)

    def test_s2(self):
        """ testing instances """
        self.assertEqual(self.obj6.id, 6)
        self.assertEqual(self.obj6.width, 7)
        self.assertEqual(self.obj6.height, 4)

    def test_arg1(self):
        """ Testing arguments empty, string """
        with self.assertRaises(TypeError):
            dummy = Rectangle()
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            dumy = Rectangle("Nasser", 17)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            dumy = Rectangle(17, "Nasser")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            dumy = Rectangle(23, 17, "Nasser")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            dumy = Rectangle(23, 17, 5, "Nasser")

    def test_arg2(self):
        """ testing negatives arguments"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            dumy = Rectangle(-6, 17)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            dumy = Rectangle(6, -17)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            dumy = Rectangle(6, 17, -4, 6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            dumy = Rectangle(6, 17, 4, -6,)

    def test_s4(self):
        """ testing area method """
        self.assertEqual(self.obj8.area(), 40)

    def test_display(self):
        """ display method """
        obj9 = Rectangle(4, 3)
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        obj9.display()
        self.assertEqual(sys.stdout.getvalue(), "####\n####\n####\n")

    def test_upd(self):
        """ testing update and str method """
        obj10 = Rectangle(17, 17, 17, 17, 17)
        self.assertEqual(str(obj10), "[Rectangle] (17) 17/17 - 17/17")
        obj10.update(23, 7, 5, 4, 3)
        self.assertEqual(str(obj10), "[Rectangle] (23) 4/3 - 7/5")
        obj10.update(15)
        self.assertEqual(str(obj10), "[Rectangle] (15) 4/3 - 7/5")
        obj10.update(16, 10, 8)
        self.assertEqual(str(obj10), "[Rectangle] (16) 4/3 - 10/8")

    def test_upd_empty(self):
        """ testing empty arguments """
        obj11 = Rectangle(17, 17, 17, 17, 17)
        obj11.update()
        self.assertEqual(str(obj11), "[Rectangle] (17) 17/17 - 17/17")

    def test_upd_ka(self):
        """ testing **kwargs """
        obj12 = Rectangle(17, 17, 17, 17, 17)
        self.assertEqual(str(obj12), "[Rectangle] (17) 17/17 - 17/17")
        obj12.update(width=10, height=6, x=3, y=2, id=11)
        self.assertEqual(str(obj12), "[Rectangle] (11) 3/2 - 10/6")
        obj12.update(width=12)
        self.assertEqual(str(obj12), "[Rectangle] (11) 3/2 - 12/6")
        obj12.update(hola=12)
        self.assertEqual(str(obj12), "[Rectangle] (11) 3/2 - 12/6")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            obj12.update(width="Nasser")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            obj12.update(x=-1)

    def test_dict(self):
        """ testing to_dictionary method """
        obj13 = Rectangle(12, 6, 5, 4, 33)
        dict13 = obj13.to_dictionary()
        self.assertEqual(dict13, {'id': 33, 'width': 12, 'height': 6,
                         'x': 5, 'y': 4})

    def test_stf(self):
        """ testing save_to_file method """
        obj13 = Rectangle(17, 17, 17, 17, 22)
        obj14 = Rectangle(17, 17, 17, 17, 20)
        list1 = [obj13, obj14]
        Rectangle.save_to_file(list1)
        with open("Rectangle.json", 'r') as f:
            list2 = [obj13.to_dictionary(), obj14.to_dictionary()]
            self.assertEqual(json.dumps(list2), f.read())

    def test_stf1(self):
        """ testing save_to_file method with None argument """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual("[]", f.read())

    def test_stf2(self):
        """ testing save_to_file method with empty list """
        list1 = []
        Rectangle.save_to_file(list1)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(json.dumps(list1), f.read())

    def test_create(self):
        """ testing create method """
        dict4 = {'id': 33, 'width': 12, 'height': 6, 'x': 5, 'y': 4}
        obj15 = Rectangle.create(**dict4)
        self.assertEqual(str(obj15), "[Rectangle] (33) 5/4 - 12/6")
