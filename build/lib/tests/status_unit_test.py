
import unittest
import numpy
from functools import reduce

from status_mgmt.Status import Status

class BaseTest(unittest.TestCase):
    def test_key_status(self):
        my_status = Status()
        my_status["one"] = 1
        self.assertEqual(1,my_status["one"])
    def test_multi_keys(self):
        my_status = Status()
        my_status[1] = 1
        my_status[2] = 2
        for i in range(1,3):
            self.assertEqual(i,my_status[i])
    def test_run_order(self):
        my_status = Status()
        my_status[1] = 1
        my_status[2] = 2
        for info in my_status.iter_run_order():
            for k,v in info.items():
                self.assertEqual(k,str(v+1))
    def test_update(self):
        my_status = Status()
        my_status.update(0)
        my_status.update(1)
        for info in my_status.iter_run_order():
            for k,v in info.items():
                self.assertEqual(k,str(v))