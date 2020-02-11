
import unittest
import numpy
from functools import reduce

from in_array.in_array import _is_float_, _is_int_

class BaseTest(unittest.TestCase):
    def test_is_float(self):
        str1 = '1.0'
        self.assertTrue(_is_float_(str1))
        str2 = '1'
        self.assertTrue(_is_float_(str2))
        str3 = 'a'
        self.assertFalse(_is_float_(str3))
    def test_is_int(self):
        str1 = '1.0'
        self.assertFalse(_is_int_(str1))
        str2 = '1'
        self.assertTrue(_is_int_(str2))
        str3 = 'a'
        self.assertFalse(_is_int_(str3))
