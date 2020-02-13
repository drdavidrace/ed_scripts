#  Standard imports
import os, sys
#Test imports
import unittest
import numpy as np
import sympy as syp
from pprint import pprint
from functools import reduce

from pretty_math import pretty_math
from pretty_math.pretty_math import _create_latex_sentence_


class NumpyArrayLatexTest(unittest.TestCase):

    def __init__(self,*args,**kwargs):
        super(NumpyArrayLatexTest,self).__init__(*args, **kwargs)
        self.epsilon = 1e-12
        pprint(pretty_math.__version__)

    def test_latex_str(self):
        str1 = '1. 2, 3.0, -4.0'
        status, res = _create_latex_sentence_(str1)
        self.assertTrue(status == 0)



