"""These functions are the widget management functions for the calculator function.

This is specifically designed for Colaboratory, so there is a mixture of Google colab widgets
and ipywidgets.  As Colaboratory supports more ipywidgets, these will migrate to ipywidgets so
they work with 
"""
from IPython.display import display
import ipywidgets as iwidgets
from ipywidgets import Button, GridBox, Layout, ButtonStyle, IntText, FloatText, Output
from typing import Dict, Tuple, List
import sympy as sp
#
def set_default_numeric_values(num_variables:int = 5) ->  Tuple:
    """Returns a default list of variables to help keep the code clean

    Inputs:
    num_variables:  The number of variables to return

    Output:
    A list of the sympy values for that number of variables where the
    default values are 0 to num_variables - 1.
    """
    assert isinstance(num_variables, int)
    return (sp.S(i) for i in range(num_variables))
#
def get_default_var_names(num_variables:int = 5, start_char:str = "a") -> List:
    assert isinstance(num_variables, int)
    assert isinstance(start_char, str)
    assert len(start_char) == 1
    if start_char.islower():
        assert ord(start_char) + num_variables <= ord('z') + 1
    elif start_char.isupper():
        assert ord(start_char) + num_variables <= ord('Z') + 1
    else:
        print("{} must be a lower case or upper case character".format(start_char))
        assert False
    return [str(chr(i)) for i in range(ord(start_char), ord(start_char) + num_variables)]
