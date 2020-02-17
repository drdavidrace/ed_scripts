#  Standard imports
import os, sys
#Test imports
import unittest
import numpy as np
import sympy as sp
from pprint import pprint
from functools import reduce

from pretty_math import pretty_math
import pretty_math.pretty_math as p_m
from pretty_math.pretty_math import _create_latex_sentence_, \
    _display_l_

_jup_math_eq_delim_ = ""
_pdf_math_eq_delim_ = "$"

class BasicDisplayLatexTest(unittest.TestCase):

    def __init__(self,*args,**kwargs):
        super(BasicDisplayLatexTest,self).__init__(*args, **kwargs)
        self.epsilon = 1e-12
        pprint('BasicDisplayLatexTest')

    def test_latex_str(self):
        str1 = '1. 2, 3.0, -4.0'
        str2 = "\\," + str1 + "\\,"
        status, res = _create_latex_sentence_(str1, p_m._jup_math_eq_delim_)
        self.assertTrue(status == 0)
        self.assertTrue(res == str2)

    def test_latex_number(self):
        x = 3.2
        x_str = "\\," + str(x) + "\\,"
        status,res = _create_latex_sentence_(x, p_m._jup_math_eq_delim_)
        self.assertTrue(status == 0)
        self.assertTrue(res == x_str)

    def test_latex_sympy(self):
        x = sp.symbols('x')
        x = 3.2
        x_str = "\\," + str(3.2) + "\\,"
        status,res = _create_latex_sentence_(x, p_m._jup_math_eq_delim_)
        self.assertTrue(status == 0)
        self.assertTrue(res == x_str)

    def test_latex_sympy_2(self):
        x = sp.symbols('x')
        y = sp.symbols('y')
        s = sp.Function('Slope')(x,y)
        s = 2.0 * x + -1.0 * sp.cos( x * y)
        x_str = " " + "$2.0 x - 1.0 \\cos{\\left(x y \\right)}$"
        status,res = _create_latex_sentence_(s, p_m._pdf_math_eq_delim_)
        self.assertTrue(status == 0)
        self.assertTrue(res == x_str)

    def test_latex_sympy_list(self):
        x = sp.symbols('x')
        y = sp.symbols('y')
        s = sp.Function('Slope')(x,y)
        s = 2.0 * x + -1.0 * sp.cos( x * y)
        in_array = ["f(x,y) = ", s]
        x_str = "\\,f(x,y) = "+ "\\, " + "$2.0 x - 1.0 \\cos{\\left(x y \\right)}$"  #The \\ are because this is a python string
        status,res = _create_latex_sentence_(in_array, p_m._pdf_math_eq_delim_)
        self.assertTrue(status == 0)
        self.assertTrue(res == x_str)

    def test_latex_sympy_sentence(self):
        x = sp.symbols('x')
        y = sp.symbols('y')
        s = sp.Function('Slope')(x,y)
        s = 2.0 * x + -1.0 * sp.cos( x * y)
        in_array = ["f(x,y) = ", s]
        x_str = "\\begin{multline*}  " + "\\,f(x,y) = " + "\\, " \
            + "$2.0 x - 1.0 \\cos{\\left(x y \\right)}$" + \
                " \\end{multline*}"  #The \\ are because this is a python string
        status,res = _display_l_(in_array, p_m._pdf_math_eq_delim_)
        self.assertTrue(status == 0)
        self.assertTrue(res == x_str)
#
class Phase1DisplayLatexTest(unittest.TestCase):

    def __init__(self,*args,**kwargs):
        super(Phase1DisplayLatexTest,self).__init__(*args, **kwargs)
        self.epsilon = 1e-12
        pprint('BasicDisplayLatexTest')

    def test_latex_sympy_sentence(self):
        x = sp.symbols('x')
        y = sp.symbols('y')
        s = sp.Function('Slope')(x,y)
        s = 2.0 * x + -1.0 * sp.cos( x * y)
        in_array = ["f(x,y) = ", s]
        x_str = "\\begin{multline*}  " + "\\,f(x,y) = " + "\\, " \
            + "$2.0 x - 1.0 \\cos{\\left(x y \\right)}$" + \
                " \\end{multline*}"  #The \\ are because this is a python string
        _, res = _display_l_(in_array, p_m._pdf_math_eq_delim_)
        self.assertTrue(res == x_str)
