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


    current_expression and last_result are side effects of calculator.
    """
    def __init__(self, numeric_var_names = ["a", "b", "c", "d", "e"], 
        matrix_var_names = ["A", "B", "C", "D", "E"], 
        operators = {"+":"+", "-":"-","*":"*","/":"/","\\":"\\","^":"**","=":"=","(":"(",")":")","\\\\":"\\\\"},
        numbers = ["1","2","3","4","5","6","7","8","9","0","."] ):

        self.operators = operators
        self.numeric_var_names = numeric_var_names
        self.matrix_var_names = matrix_var_names
        self.numbers = numbers
        #Functions List
        self.functions = {"cos":"sp.cos(", "sin":"sp.sin(","tan":"sp.tan(", "pi":"sp.pi", "e":"sp.e",
        "asin":"sp.asin(", "acos":"sp.acos(", "atan":"sp.atan(","atan2":"atan2(","exp":"sp.exp(","log":"sp.log("}
        #Compute the size
        total_numbers_and_vars = max([len(matrix_var_names) + 4, len(numeric_var_names) + 4])
        base_rows = max([len(numeric_var_names),len(matrix_var_names),len(self.operators), total_numbers_and_vars])
        self.num_rows = base_rows + 3
        self.num_cols = 7
        #Define the operator keys
        self.operators_keys = [i for i in self.operators.keys()]
        #Define the basic columns
        self.operator_col = self.num_cols - 2
        self.numeric_names_col = self.operator_col - 1
        self.matrix_names_col = self.numeric_names_col - 1
        self.numbers_col = self.num_cols - 3
        self.start_functions_col = 0
        self.end_functions_col = self.numbers_col
        #Define the basic rows
        self.operator_row = 1
        self.numeric_names_row = 1
        self.matrix_names_row = 1
        self.numbers_row = max([self.numeric_names_row + len(numeric_var_names), 
            self.matrix_names_row + len(matrix_var_names)])
        self.command_row = self.num_rows - 2
        self.result_row = self.num_rows - 1
        self.functons_row = 0

        self.cur_command = ""
        self.calculator = GridspecLayout(self.num_rows, self.num_cols)
        self.command_cell = None
        self.result_cell = None
        self.exe_cell = None
        self.clr_cell = None
        self.operator_cells = [None] * len(self.operators)
        self.matrix_name_cells = [None] * len(matrix_var_names)
        self.numeric_name_cells = [None] * len(numeric_var_names)
        self.numbers_cells = [None] * len(numbers)
        self.function_cells = [None] * len(self.functions)
        #  Compute variables
        self.temp_val_1234 = None

        self.build_interface()
        display(self.calculator)
    #  On click actions
    def _on_clr_clicked_(self, b):
        self.command_cell.clear_output()
        self.cur_command = ""
        self.result_cell.clear_output()
    #
    def _on_exe_clicked_(self,btn):
        #eventually add a check for =
        self.result_cell.clear_output()
        self.temp_val_1234 = None
        current_command = self.cur_command
        if "=" in current_command:
            command_vals = current_command.split("=")
            if len(command_vals) > 2:
                with self.result_cell:
                    print("Error:  There can only be one = in the command.")
            else:
                var_name = command_vals[0].strip()
                if (var_name in self.numeric_var_names) or (var_name in self.matrix_var_names):
                    work_string = current_command
                    for x in self.numeric_var_names:
                        search_pattern = " " + x + " "
                        work_string = work_string.replace(search_pattern, " globals()[" + x + "] ")
                    exec("{}".format(work_string))

                    with self.result_cell:
                        print("Check the variable definition in the next cell.")
                else:
                    with self.result_cell:
                        print("You must use one of the current variable names.")
        else:
            #replace the plain variable names with the globals names
            work_string = current_command
            for x in self.numeric_var_names:
                search_pattern = " " + x + " "
                work_string = work_string.replace(search_pattern, " globals()[\"" + x + "\"] ")
            with self.result_cell:
                print(work_string)
            exec("self.temp_val_1234 = {}".format(work_string))
            with self.result_cell:
                print(self.temp_val_1234)
    #
    def _on_variable_clicked_(self, b):
        self.command_cell.clear_output()
        self.cur_command += b.description
        with self.command_cell:
            print(self.cur_command)
    def _on_operator_clicked_(self, b):
        self.command_cell.clear_output()
        self.cur_command += self.operators[b.description]
        with self.command_cell:
            print(self.cur_command)
    def _on_function_clicked_(self, b):
        self.command_cell.clear_output()
        self.cur_command += self.functions[b.description]
        with self.command_cell:
            print(self.cur_command)

    #Define the calculator interface
    def build_interface(self):
        #Define the command cell
        self.command_cell = Output(layout=Layout(width='auto',border='1px solid black'))
        self.calculator[self.command_row,0:self.num_cols-1] = self.command_cell
        self.command_cell.clear_output()
        with self.command_cell:
            print("")
        #Define the result cell
        self.result_cell = Output(layout=Layout(width='auto',border='1px solid black'))
        self.calculator[self.result_row,0:self.num_cols] = self.result_cell
        self.result_cell.clear_output()
        with self.result_cell:
            print("")
        #Define the exe button
        self.exe_cell = Button(description="exe")
        self.calculator[self.command_row,self.num_cols-1] = self.exe_cell
        self.exe_cell.on_click(self._on_exe_clicked_)
        #Simple operations
        self.clr_cell = Button(description="clr")
        self.calculator[0,self.num_cols-1] = self.clr_cell
        self.clr_cell.on_click(self._on_clr_clicked_)
        work_col = self.operator_col
        base_row = self.operator_row
        for i in range(len(self.operators)):
            if i == len(self.numeric_var_names): #Warning this assume both sets of variables are same length
                work_col += 1
                base_row = self.operator_row - len(self.numeric_var_names)
            self.operator_cells[i] = Button(description=" " + self.operators_keys[i] + " ")
            self.calculator[base_row + i,work_col] = self.operator_cells[i]
            self.operator_cells[i].on_click(self._on_operator_clicked_)
        #Display the variables
        for i in range(len(self.numeric_var_names)):
            self.numeric_name_cells[i] = Button(description= " " + self.numeric_var_names[i] + " ")
            self.calculator[self.numeric_names_row + i,self.numeric_names_col] = self.numeric_name_cells[i]
            self.numeric_name_cells[i].on_click(self._on_variable_clicked_)
        for i in range(len(self.matrix_var_names)):
            self.matrix_name_cells[i] = Button(description=" " + self.matrix_var_names[i] + " ")
            self.calculator[self.matrix_names_row + i, self.matrix_names_col] = self.matrix_name_cells[i]
            self.matrix_name_cells[i].on_click(self._on_variable_clicked_)
        #Build the numbers keypad
        start_row = self.numbers_row + 2
        #numbers 1 - 9
        for i in range(9):
            self.numbers_cells[i] = Button(description = self.numbers[i])
            i_row = start_row - i // 3
            i_col = self.numbers_col + i - 3 * (i // 3)
            self.calculator[i_row,i_col] = self.numbers_cells[i]
            self.numbers_cells[i].on_click(self._on_variable_clicked_)
        #0 and .
        self.numbers_cells[9] = Button(description = self.numbers[9])
        self.calculator[start_row + 1, self.numbers_col] = self.numbers_cells[9]
        self.numbers_cells[9].on_click(self._on_variable_clicked_)
        self.numbers_cells[10] = Button(description = self.numbers[10],layout=Layout(width='auto'))
        self.calculator[start_row + 1, self.numbers_col+1:self.numbers_col+3] = self.numbers_cells[10]
        # self.calculator[start_row + 1, self.numbers_col+2] = self.numbers_cells[10]
        self.numbers_cells[10].on_click(self._on_variable_clicked_)
        # Define the functions
        i = 0
        for f in self.functions:
            i_row = i //  (self.end_functions_col - 1)
            i_col = i - i_row * (self.end_functions_col -1)
            self.function_cells[i] = Button(description=f)
            self.calculator[i_row,i_col] = self.function_cells[i]
            self.function_cells[i].on_click(self._on_function_clicked_)
            i += 1


   