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
        pos_names = pos_names + row_pos_names + "\n"
    #Build the Display
    grid_template_rows = "".join(["auto " for i in range(num_row + 1)])
    width_column = int(100//num_col)
    width_first_col = 100 - width_column * num_col
    grid_template_columns = "{}% ".format(width_first_col) + "".join(["{}%".format(width_column) for i in range(num_col)])
    print(grid_template_columns)
    print(grid_template_rows)
    print(pos_names)
    #display the inputs
    matrix_grid = GridBox(children=children,
        layout = Layout(
            width="75%",
            grid_template_rows = grid_template_rows,
            grid_template_columns = grid_template_columns,
            grid_template_areas = pos_names
            )
        )
    # display(matrix_grid)
    #
    return matrix_grid, inputs
