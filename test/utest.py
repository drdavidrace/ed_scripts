#!/usr/bin/env python
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
up_path = os.path.dirname(dir_path)
sys.path.append(up_path)
import unittest

from in_array.in_array import _is_float_, _is_int_

class UnitTest(unittest.TestCase):
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
if __name__ == '__main__':
    print("Entering Test Cases")
    unittest.main()
    print('Leaving Test Cases')
