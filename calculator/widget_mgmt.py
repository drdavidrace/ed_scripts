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
class calculator():
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
    def __init__(self):
        self.num_rows = 7
        self.num_cols = 7
        self.cur_command = ""
        self.calculator = GridspecLayout(self.num_rows, self.num_cols)
        self.output_cell = None
        self.exe_cell = None
        self.clr_cell = None
        self.plus_cell = None
        self.minus_cell = None
        self.build_interface()
        display(self.calculator)
    #  On click actions
    def _on_clr_clicked_(self, b):
        self.output_cell.clear_output()
        self.cur_command = ""
    def _on_plus_clicked_(self, b):
        self.output_cell.clear_output()
        self.cur_command += "+"
        with self.output_cell:
            print(self.cur_command)
    def _on_minus_clicked_(self, b):
        self.output_cell.clear_output()
        self.cur_command += "-"
        with self.output_cell:
            print(self.cur_command)

    #Define the calculator interface
    def build_interface(self):
        #Define the output cell
        self.output_cell = Output(layout=Layout(width='auto',border='1px solid black'))
        for i in range(self.num_cols-1):
            self.calculator[self.num_rows-1,i] = self.output_cell
        self.output_cell.clear_output()
        self.output_cell.append_stdout(self.cur_command)
        #Define the exe button
        self.exe_cell = Button(description="exe")
        self.calculator[self.num_rows-1,self.num_cols-1] = self.exe_cell
        #Simple operations
        self.clr_cell = Button(description="clr")
        self.calculator[0,self.num_cols-1] = self.clr_cell
        self.clr_cell.on_click(self._on_clr_clicked_)
        self.plus_cell = Button(description="+")
        self.calculator[1,self.num_cols-1]=self.plus_cell
        self.plus_cell.on_click(self._on_plus_clicked_)
        self.minus_cell = Button(description="-")
        self.calculator[2,self.num_cols-1]=self.minus_cell
        self.minus_cell.on_click(self._on_minus_clicked_)
        #Display the calculator

   