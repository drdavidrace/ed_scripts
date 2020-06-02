"""These functions are the widget management functions for the calculator function.

This is specifically designed for Colaboratory, so there is a mixture of Google colab widgets
and ipywidgets.  As Colaboratory supports more ipywidgets, these will migrate to ipywidgets so
they work with 
"""
from IPython.display import display
import ipywidgets as iwidgets
from ipywidgets import Button, GridBox, GridspecLayout, Layout, ButtonStyle, IntText, FloatText, Output
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
    return (i for i in range(num_variables))
#
def set_default_matrix_values(num_variables:int = 5) ->  Tuple:
    """Returns a default list of variables to help keep the code clean

    Inputs:
    num_variables:  The number of variables to return

    Output:
    A list of the sympy values for that number of variables where the
    default values are 0 to num_variables - 1.
    """
    assert isinstance(num_variables, int)
    return (sp.Matrix([[i]]) for i in range(num_variables))
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
#
def build_matrix_input(num_row:int = None, num_col:int = None) ->  List:
    assert num_row is not None
    assert isinstance(num_row, int)
    assert num_row >= 1 and num_row <= 10
    assert num_col is not None
    assert isinstance(num_col, int)
    assert num_col >= 1 and num_col <= 10
    inputs = []
    for i in range(num_row+1):
        row_list = [None for j in range(num_col+1)]
        inputs.append(row_list)
    pos_names = ""
    children = []
    #Build the inputs
    for i in range(num_row + 1):
        row_pos_names = ""
        for j in range(num_col+1):
 
            pos_i_j = None
            if i == 0:
                if j == 0:
                    pos_i_j = "pos_{}_{}".format(i,j)
                    inputs[i][j] = Output(layout=Layout(width='auto',grid_area = pos_i_j))
                    with inputs[i][j]:
                        print("")
                else:
                    pos_i_j = "pos_{}_{}".format(i,j)
                    inputs[i][j] = Output(layout=Layout(width='auto',grid_area = pos_i_j))
                    with inputs[i][j]:
                        print("       {}       ".format(j))
                row_pos_names = row_pos_names + pos_i_j + " "
            else:
                if j == 0:
                    pos_i_j = "pos_{}_{}".format(i,j)
                    inputs[i][j] = Output(layout=Layout(width='auto',grid_area=pos_i_j))
                    with inputs[i][j]:
                        print(" {} ".format(i))
                else:
                    pos_i_j = "pos_{}_{}".format(i,j)
                    inputs[i][j] = FloatText(value=0.,disabled=False,layout=Layout(width='auto',grid_area=pos_i_j))
                row_pos_names = row_pos_names + pos_i_j + " "
            children.append(inputs[i][j])
        pos_names = pos_names + '"' + row_pos_names + '"' + " "
    #Build the Display
    # grid_template_rows = '"' + " ".join(["auto " for i in range(num_row + 1)]) + '"'
    width_column = int(96//num_col)
    width_first_col = 100 - width_column * num_col
    # grid_template_columns = '"' + "{}% ".format(width_first_col) + " ".join(["{}%".format(width_column) for i in range(num_col)]) + '"'
    work_width = None
    if num_col <= 3:
        work_width = '"{}%"'.format(50)
    elif num_col <= 6:
        work_width = '"{}%"'.format(75)
    else:
        work_width = '"{}%"'.format(100)

    matrix_grid = GridspecLayout(num_row+1, num_col+1, 
        layout=Layout(
            width=""" + work_width + """,
            width_ratios = "[1,3,3,3]"
            )
    )
    for i in range(num_row+1):
        for j in range(num_col+1):
            matrix_grid[i,j] = inputs[i][j]
 
    display(matrix_grid)
    #
    return inputs, matrix_grid
