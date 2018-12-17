
import unittest
import numpy as np
import sympy as syp
from pprint import pprint
from functools import reduce

from in_array.in_array import _is_float_, _is_int_
from in_array.in_array import str_array_floats, array_float_np, array_float_syp, matrix_float_syp
from in_array.in_array import str_array_ints, array_int_np, array_int_syp, matrix_int_syp

class NumpyArrayFloatTest(unittest.TestCase):

    def __init__(self,*args,**kwargs):
        super(NumpyArrayFloatTest,self).__init__(*args, **kwargs)
        self.epsilon = 1e-12

    def test_is_float(self):
        str1 = '1. 2, 3.0, -4.0'
        res = str_array_floats(str1)
        r = [isinstance(x,np.float64) for x in res]
        r = reduce(lambda x,y: x and y, r)
        self.assertTrue(r)
        str2 = '1. 2, 3.0, -4.0, a'
        res = str_array_floats(str2)
        self.assertIsNone(res)
    def test_two_dim_array_np(self):
        a1 = ['1. 2, 3.0, -4.0','1. 2, -3.0, -4.0']
        a = array_float_np(a1)
        b = np.array([str_array_floats(r) for r in a1])
        pass_val = np.any(np.less_equal(np.abs(a - b), self.epsilon))
        self.assertTrue(pass_val)
        a_shape = np.array(a.shape)
        t_shape = np.array((2,4))
        self.assertTrue(np.any(np.equal(a_shape,t_shape)))
    def test_bad_np(self):
        a1 = ['1. 2, 3.0, a','1. 2, -3.0, -4.0']
        a = array_float_np(a1)
        self.assertIsNone(a)
        a1 = ['1. 2, 3.0, -4.0','1. 2, -3.0, -4.0']
        a2 = ['1. 2, 3.0, a','1. 2, -3.0, -4.0']
        aa = [a1,a2]
        a = array_float_np(aa)
        self.assertIsNone(a)
    def test_multi_dim_array_np(self):
        a1 = ['1. 2, 3.0, -4.0','1. 2, -3.0, -4.0']
        a2 = ['1. 2, 3.0, -4.0','1. 2, -3.0, -4.0']
        aa = [a1,a2]
        a = array_float_np(aa)
        b = np.array([array_float_np(r) for r in aa])
        pass_val = np.any(np.less_equal(np.abs(a - b), self.epsilon))
        self.assertTrue(pass_val)
        a_shape = np.array(a.shape)
        t_shape = np.array((2,2,4))
        self.assertTrue(np.any(np.equal(a_shape,t_shape)))

class NumpyArrayIntTest(unittest.TestCase):

    def test_is_int(self):
        str1 = '1 2, 3, -4'
        res = str_array_ints(str1)
        r = [isinstance(x,np.int64) for x in res]
        r = reduce(lambda x,y: x and y, r)
        self.assertTrue(r)
        str1 = '1 2, ,3,, -4'
        res = str_array_ints(str1)
        r = [isinstance(x,np.int64) for x in res]
        r = reduce(lambda x,y: x and y, r)
        self.assertTrue(r)
        res_shape = res.shape
        t_shape = np.array((4,))
        self.assertTrue(np.any(np.equal(res_shape,t_shape)))
        str2 = '1. 2, 3.0, -4.0'
        res = str_array_ints(str2)
        self.assertIsNone(res)
        str3 = '1 2, 3, -4, a'
        res = str_array_ints(str3)
        self.assertIsNone(res)
    def test_two_dim_array_int(self):
        a1 = ['1 2, 3, -4','1 2, -3, -4']
        a = array_int_np(a1)
        b = np.array([[1,1,3,-4],[1,2,-3,-4]])
        pass_val = np.any(np.equal(a,b))
        self.assertTrue(pass_val)
        a_shape = np.array(a.shape)
        t_shape = np.array((2,4))
        self.assertTrue(np.any(np.equal(a_shape,t_shape)))
    def test_multi_dim_array_np(self):
        a1 = ['1 2, 3, -4','1 2, -3, -4']
        a2 = ['1 2, 3, -4','1 2, -3, -4']
        aa = [a1,a2]
        a = array_int_np(aa)
        b = np.array([array_int_np(r) for r in aa])
        pass_val = np.any(np.equal(a,b))
        self.assertTrue(pass_val)
        a_shape = np.array(a.shape)
        t_shape = np.array((2,2,4))
        self.assertTrue(np.any(np.equal(a_shape,t_shape)))
    def test_bad_np(self):
        a1 = ['1 2, 3, a','1 2, -3, -4']
        a = array_int_np(a1)
        self.assertIsNone(a)
        a1 = ['1 2, 3, 4.','1 2, -3, -4']
        a = array_int_np(a1)
        self.assertIsNone(a)
        a1 = ['1 2, 3.0, -4.0','1. 2, -3.0, -4.0']
        a2 = ['1. 2, 3.0, a','1. 2, -3.0, -4.0']
        aa = [a1,a2]
        a = array_int_np(aa)
        self.assertIsNone(a)

class SympyArrayIntTest(unittest.TestCase):

    def test_is_int(self):
        str1 = '1 2, 3, -4'
        res = str_array_ints(str1)
        r = [isinstance(x,np.int64) for x in res]
        r = reduce(lambda x,y: x and y, r)
        self.assertTrue(r)
        str1 = '1 2, ,3,, -4'
        res = str_array_ints(str1)
        r = [isinstance(x,np.int64) for x in res]
        r = reduce(lambda x,y: x and y, r)
        self.assertTrue(r)
        res_shape = res.shape
        t_shape = np.array((4,))
        self.assertTrue(np.any(np.equal(res_shape,t_shape)))
        str2 = '1. 2, 3.0, -4.0'
        res = str_array_ints(str2)
        self.assertIsNone(res)
        str3 = '1 2, 3, -4, a'
        res = str_array_ints(str3)
        self.assertIsNone(res)
    def test_two_dim_array_int_syp(self):
        a1 = ['1 2, 3, -4','1 2, -3, -4']
        a = array_int_syp(a1)
        a_shape = a.shape
        b = syp.Array([[1,2,3,-4],[1,2,-3,-4]])
        a_n = np.array(a).astype(np.int64).reshape(a_shape)
        b_n = np.array(b).astype(np.int64).reshape(a_shape)
        self.assertTrue(np.any(np.equal(a_n,b_n)))
        a_shape = np.array(a_n.shape)
        t_shape = np.array((2,4))
        self.assertTrue(np.any(np.equal(a_shape,t_shape)))

    def test_multi_dim_array_syp(self):
        a1 = ['1 2, 3, -4','1 2, -3, -4']
        a2 = ['1 2, 3, -4','1 2, -3, -4']
        aa = [a1,a2]
        a = array_int_syp(aa)
        a_shape = a.shape
        b = array_int_np(aa)
        a_n = np.array(a).astype(np.int64).reshape(a_shape)
        self.assertTrue(np.any(np.equal(a_n,b)))
        a_shape = np.array(a.shape)
        t_shape = np.array((2,2,4))
        self.assertTrue(np.any(np.equal(a_shape,t_shape)))

    def test_bad_np(self):
        a1 = ['1 2, 3, a','1 2, -3, -4']
        a = array_int_syp(a1)
        self.assertIsNone(a)
        a1 = ['1 2, 3, 4.','1 2, -3, -4']
        a = array_int_syp(a1)
        self.assertIsNone(a)
        a1 = ['1 2, 3.0, -4.0','1. 2, -3.0, -4.0']
        a2 = ['1. 2, 3.0, a','1. 2, -3.0, -4.0']
        aa = [a1,a2]
        a = array_int_syp(aa)
        self.assertIsNone(a)

class SympyMatrixIntTest(unittest.TestCase):

    def test_two_dim_array_int_syp(self):
        a1 = ['1 2, 3, -4','1 2, -3, -4']
        a = matrix_int_syp(a1)
        a_shape = a.shape
        b = syp.Matrix([[1,2,3,-4],[1,2,-3,-4]])
        a_n = np.array(a).astype(np.int64).reshape(a_shape)
        b_n = np.array(b).astype(np.int64).reshape(a_shape)
        self.assertTrue(np.any(np.equal(a_n,b_n)))
        a_shape = np.array(a_n.shape)
        t_shape = np.array((2,4))
        self.assertTrue(np.any(np.equal(a_shape,t_shape)))

    def test_bad_matrix_syp(self):
        a1 = ['1 2, 3, -4','1 2, -3, -4']
        a2 = ['1 2, 3, -4','1 2, -3, -4']
        aa = [a1,a2]
        a = matrix_int_syp(aa)
        self.assertIsNone(a)
