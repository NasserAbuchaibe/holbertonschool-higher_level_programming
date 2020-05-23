#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class Test_mxInteg(unittest.TestCase):

    def test_maxInteger(self):
        _list = [10, 4, 21, 9]
        reret = max_integer(_list)
        self.assertEqual(reret, 21)

    def test_1_elem(self):
        _list = [10]
        reret = max_integer(_list)
        self.assertEqual(reret, 10)

    def test_neg_numb(self):
        _list = [-12, -34, -2, -1]
        reret = max_integer(_list)
        self.assertEqual(reret, -1)

    def test_arg_none(self):
        _list = []
        reret = max_integer(_list)
        self.assertEqual(reret, None)

    def test_str(self):
        _list = "Nasser"
        reret = max_integer(_list)
        self.assertEqual(reret, 's')

    def test_tup(self):
        _list = (7, 23)
        reret = max_integer(_list)
        self.assertEqual(reret, 23)

    def test_nega_numb(self):
        self.assertRaises(TypeError, max_integer, -8)

    def test_numb(self):
        self.assertRaises(TypeError, max_integer, 10)

    def test_strList(self):
        _list = [10, 4, 21, "9"]
        self.assertRaises(TypeError, max_integer, _list)

if __name__ == '__main__':
    unittest.main()
