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
    num_variables:  The number of variables to return.   Defaults to 5 and right now should not be
    more until we can control the size of the outputs more.

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
    num_variables:  The number of variables to return.  Defaults to 5 and right now should not be
    more until we can control the size of the outputs more.

    Output:
    A list of the sympy values for that number of variables where the
    default values are 0 to num_variables - 1.
    """
    assert isinstance(num_variables, int)
    return (sp.Matrix([[i]]) for i in range(num_variables))
#
def get_default_var_names(num_variables:int = 5, start_char:str = "a") -> List:
    """Returns the default variable names starting with start_char
    Inputs:
    num_variables:  The number of variable names to return.  Defaults to 5 and right now should not be more
    until we can control the size of the outputs more.

    Output:
    A list of the variable names to use in the calculator.
    """
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
    """Builds the window using ipywidgets to input matrix values.

    Inputs:  
    num_row - The number of rows for the matrix, 1 <= num_row <=10
    num_col - The number of columns for the matrix, 1 <= num_col <= 10

    (This is a calculator for class work so I don't want large sizes.)

    Outputs:

    matrix_grid -  This is displayed for entry of the values.  This is really a set of widgets so is 
    interactive.

    inputs - This is the set of actual widgets that the Colaboratory application can use for 
    reading the input values.

    ToDo:  Pass in a matrix for the default values.
    """

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
    matrix_grid = None
    if num_col <= 3:
        matrix_grid = GridspecLayout(num_row+1, num_col+1, 
            layout=Layout(
                width="50%"
                )
        )
    elif num_col <= 5:
        matrix_grid = GridspecLayout(num_row+1, num_col+1, 
            layout=Layout(
                width="75%"
                )
        )  
    else:
        matrix_grid = GridspecLayout(num_row+1, num_col+1)     
    for i in range(num_row+1):
        for j in range(num_col+1):
            matrix_grid[i,j] = inputs[i][j]
    #  Display the 
    display(matrix_grid)
    #
    return inputs
#
def build_calculator():
    """  This is the basic calculator interface for the calculator.  It will use
    a set of buttons to build an expression, then execute that using exec.  Not elegant
    yet, but it should be functional.

    Inputs:  None
    The calculator face is hard coded in this version.

    Outputs:
    calculator - This is displayed in colaboratory for building the expression to execute.
    current_expression - This is the current expression that is built.
    last_result - When the expression is executed, this will be where the result is stored.

    There is no actual return from this function.

    current_expression and last_result are side effects of calculator.
    """
    #  On click actions
    def on_clr_clicked(b):
        output_cell.clear_output
    #Very detailed setting this up since all of the buttons must be built
    num_rows = 7
    num_cols = 7
    calculator = GridspecLayout(num_rows,num_cols)
    #Define the output area
    # output_area="output"
    output_cell = Output(layout=Layout(width='auto',border='1px solid black'))
    for i in range(num_cols-1):
        calculator[num_rows-1,i] = output_cell
    output_cell.append_stdout("Use the buttons to enter the command to execute.")
    #Define the exe button
    # exe_area = "exe"
    exe_cell = Button(description="exe")
    calculator[num_rows-1,num_cols-1] = exe_cell
    #Simple operations
    clr_cell = Button(description="clr")
    calculator[0,num_cols-1] = clr_cell
    clr_cell.on_click(on_clr_clicked)
    plus_cell = Button(description="+")
    calculator[1,num_cols-1]=plus_cell
    #Display the calculator
    display(calculator)
    return calculator