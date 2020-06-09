import unittest
from models.base import Base
import pep8


class Test_Base(unittest.TestCase):
    """ Testing the Base class """

    def test_style_base(self):
        """test pep8
        """
        style = pep8.StyleGuide(quiet=True)
        m = style.check_files(["models/base.py"])
        self.assertEqual(m.total_errors, 0)

    def test_id(self):
        """ set id """
        obj = Base(23)
        self.assertEqual(obj.id, 23)

    def test_id_none(self):
        """ None default id """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

    def test_id_set_control(self):
        """ id generation control """
        obj2 = Base()
        self.assertEqual(obj2.id, 2)

    def test_multi_id(self):
        """ Multiple arguments for id """
        with self.assertRaises(TypeError):
            obj3 = Base(17, 23)

    def test_instance(self):
        """ testing instance """
        obj4 = Base()
        self.assertIsInstance(obj4, Base)

    def test_tjs(self):
        """ static method test to_json_string """
        dict1 = {"id": 1, "width": 10, "height": 7, "x": 5, "y": 5}
        dict2 = {"id": 2, "width": 8, "height": 5, "x": 3, "y": 3}
        dict3 = {"id": 3, "width": 6, "height": 3, "x": 2, "y": 2}
        json_string = Base.to_json_string([dict1, dict2, dict3])
        self.assertEqual(type(json_string), str)

    def test_tjs_None(self):
        """ testing None arg """
        json_string1 = Base.to_json_string(None)
        self.assertEqual(json_string1, "[]")

    def test_tjs_empt(self):
        """ empty list """
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_fjs(self):
        """ static method test from_json_string """
        str_json = '[{"id": 1, "width": 10, "height": 7, "x": 5, "y": 5},\
                     {"id": 2, "width": 8, "height": 5, "x": 3, "y": 3},\
                     {"id": 3, "width": 6, "height": 3, "x": 2, "y": 2}]'
        list1 = Base.from_json_string(str_json)
        self.assertEqual(type(list1), list)
        self.assertEqual(type(list1[1]), dict)
