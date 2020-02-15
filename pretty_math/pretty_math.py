##############################################################
#  Purpose:  This set of routines moves away from overloading "print" to
#   a display capability.  As a rule, display seems to be a better verb to
#   describe mathematics presentation since print evolved from the concept
#   associated with output to terminals.  
#
#  This will support display to terminals; however, the display will generally
#   be considered more "complex" than simple line oriented output.
#
#  Theory:  This set of functions will be function oriented rather than object
#   oriented so that the input is more similar to print.  As a rule, these routines
#   use a good bit of str.format() functionality to build lines of output, then display
#   the output as appropriate to the output
#
#  The main interfaces will be:
#   display_lp - display in latex for output to a file
#       NOTE:  Ordinarily the latex output will be converted to pdf for review
#   display_t - display to a terminal
#       NOTE:  This is not considered very good output, but rather just a "summary"
#       that is not very enticing.  When used with output to a terminal (vs Jupyter)
#       this should be coupled with output to latex that is then converted to pdf
#   display_j - display to jupyter (colab) using mathjax
#
#  Input Format:
#   The main input format will be a list of items to display on a line.  The output
#   is concatenated together with a space between to better display information.
#
#  Main Libraries
#   sympy - sympy has a lot of flexibility for doing mathematics; therefore,
#   it is the foundation for most of the output.  It has a very powerful mathematics
#   management engine that does automatic converstion from math to latex.
##################################################################
#
from IPython.display import display, HTML, Math, Latex
import numbers
import sympy
import numpy
#from sympy import *
import sympy as sp
import numpy as np
import pkg_resources
__version__ = pkg_resources.require('ed_scripts')[0].version
#default numpy types
np_arrays = (np.ndarray)
#  sentence elements
_begin_mult_sentence_ = "\\begin{multline*}  "
_end_mult_sentence_ = " \\end{multline*}"
_mathjax_sentence_ = "<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=default'></script>"
#
def display_j(in_list: list = None) -> int:
    """This is a top level routine which displays output in Jupyter using mathjax
        NOTE:  This is currently only tested with Google Colaboratory
    
    Keyword Arguments:
        left_side {list} -- The list of stuff to display (default: {None})
    
    Returns:
        int -- discription of the status
    """
    status = 0
    try:
        assert in_list is not None
    except:
        status = 1
        print("The in_list must not be None.")
        return status
    #Main body of work
    try:
        display(HTML("<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=default'></script>"))
        #Obtain the latex
        status, full_sentence = _display_l_(in_list)
        print(status)
        print(full_sentence)
        #Use display(Math) to output the latex of the sympy expression to the output of a compute cell
        display(Math(full_sentence))
    except Exception as e:
        status = 2
        print("Something went amiss with the mathjax process.  Details: {}".format(e))
        return status
    return status
#
#  Private routines
#
def _display_l_(in_list: list = None) -> (int, str):
    """Create the output for latex version of output that is suitable for display by higher level
        routines

       Caveat:  It is assumed that the printing of the output to the file
       is handled separately from this function.
    
    Keyword Arguments:
        in_list {list} -- The list of items to display (default: {None})
        f {file-like object}  --  If f is None, then the result is returned to the caller
            If f is not None, then the result is written to f
    
    Returns:
        int -- the status of the processing
        str -- the latex string to output that is suitable for multiline output

    Assumptions:
        Currently only strings, numbers, numpy.arrays and sympy expressions are allowed as inputs in the list.

        These are converted to sympy expressions for the last three and output using latex math
    """
    status = 0
    output = None
    try:
        assert in_list is not None
    except:
        status = 1
        output = "The input must not be None."
        return status, output
    work = []
    try:
        assert isinstance(in_list, list)
        work = in_list
    except:
        work = [in_list]
    #  If we reach this point, we should have a list
    status, message = _create_latex_sentence_(work)
    #Write the output
    if (status > 0) or (len(message) == 0):
        status = 2
        return status, message
    else:
        display_message = _begin_mult_sentence_ + message + _end_mult_sentence_
        return status, display_message
#
def _create_latex_sentence_(input_val: list = None) -> (int, str):
    """
    Internal routine to create a latex sentence from components of a list or tuple
    
    Keyword Arguments:
        input_array {list, tuple} -- a list or tuple of elements to create a latex sentence (default: {None})
    
    Returns:
        int - status of the processing
        str - the latex output of the list in the form of a string
    """
    work = []
    try:
        if isinstance(input_val, list):
            work = input_val
        elif isinstance(input_val, str):
            work = [input_val]
        elif isinstance(input_val,numbers.Number):
            work = [input_val]
        elif isinstance(input_val,sp.Basic):
            work = [input_val]
        else:
            work = list(input_val)
    except:
        status = 1
        message = "The input must be able to be turned into a list"
        return status, message
    status = 0
    out_str = ""
    for v in work:
        if isinstance(v,str):
            out_str += (" " + v)
        elif isinstance(v,numbers.Number):  #This works for numpy numbers also
            out_str += (" {}".format(v))
        elif isinstance(v, np_arrays):
            x = sp.symbols('x')
            x = sp.Matrix(v)
            out_str += (" $" + sp.latex(x,mode='plain') + "$")
        else:
            try:
                assert v.has(sp.Basic)
                out_str += (" $" + sp.latex(v,mode='plain') + "$")
            except:
                status = 2
                message = "The inputs must be a str, number, np number, np.array or sympy expression: {}".format(v)
                return status, message
    message = out_str
    return status, message
#
def _get_latex_sympy_(left_side = None, input_sympy = None) -> str:
    """Internal routine to get the latex for for a sympy element using MathJax
    
    Keyword Arguments:
        left_side {str} -- Defines a simple left side for the output (default: {None})
          NOTE:  The left_side is meant to be discriptive, so an = is not included.  The user can use =, but
          there are usually better ways to convey the message.
          NOTE:  If the intent is an equation, then it is better to use display_equation
        input_sympy {A sympy object} -- Uses sympy to get the latex version of the sympy statement (default: {None})
    
    Returns:
        str -- The latex string if there is one; otherwise None
    """
    #  These data checks don't need to be here now, but this will be used in other places so
    #  a few extra data checks doesn't hurt
    try:
        assert left_side is not None
        assert input_sympy is not None
    except:
        return None   
    try:
        assert input_sympy.has(sp.Basic)
    except:
        return None
    try:
        enhance_left = left_side.replace(" ","\\,")
        latex_sentence = "{}{}".format(enhance_left, sp.latex(input_sympy,mode='plain'))
        full_sentence = "\\begin{multline*}  " + latex_sentence + " \\end{multline*}"
        return full_sentence
    except:
        return None
#
def display_j(left_side = None, right_side=None) -> int:
    """This routine displays
    
    Keyword Arguments:
        left_side {[type]} -- [description] (default: {None})
        right_side {[type]} -- [description] (default: {None})
    
    Returns:
        int -- [description]
    """
#
def display_sympy(left_side = None, input_sympy = None) -> int:
    """This routine displays a sympy element in Jupyter as the output from a code cell
    
    Keyword Arguments:
        left_side {str} -- Defines a simple left side for the output (default: {None})
          NOTE:  The left_side is meant to be discriptive, so an = is not included.  The user can use =, but
          there are usually better ways to convey the message.
          NOTE:  If the intent is an equation, then it is better to use display_equation
        input_sympy {A sympy object} -- Uses sympy to get the latex version of the sympy statement (default: {None})
    
    Returns:
        int -- status for process, since this uses a call to an outside site (mathjax) it may not be 100% accurate
        
    Side Effects:
        This routine prints a message if there is a failure.  It is assumed to be in a display environment, so this methodology
        seems to be a good trade-off since we don't want to do error checking as part of the educational code.
    """
    #
    status = 0
    #
    try:
        assert left_side is not None
        assert input_sympy is not None
    except:
        status = 1
        print("Both of the inputs must be provided.  This is a left_side and right_side requirement.")
        print("Left Side: {}".format(left_side))
        print("Right Side: {}".format(input_sympy))
        return status
    #
    try:
        assert input_sympy.has(sp.Basic)
    except:
        status = 2
        print("The right side must be a sympy expression.")
        print("The right side type: {}".format(type(input_sympy)))
        return status
    #Main body of work
    try:
        display(HTML("<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=default'></script>"))
        #Obtain the latex
        full_sentence = _get_latex_sympy_(left_side,input_sympy)
        #Use display(Math) to output the latex of the sympy expression to the output of a compute cell
        display(Math(full_sentence))
    except Exception as e:
        status = 4
        print("Something went amiss with the mathjax process.  Details: {}".format(e))
        return status
    return status

def matheq_show(left, right):
    """
    Purpose:  Display the left and right side of an equation in a compute cell
    
    
    Arguments:
        left {type: str} -- A string containing the left side  of the equation in latex
        right {type:string} -- A string containing the right side of the equation in latex

    Output:
        The equation is displayed in the output area of a cell 
    """
    import sympy as syp
    display(Math("${} = {}$".format(syp.latex(left),syp.latex(right))))

def label_value_show(label, value):
    """
    Purpose:  Display the information in the output of the compute cell in this format:
        label -> value
    
    Arguments:
        left {type: str} -- A string containing the label in latex
        right {type:string} -- A string containing the value associated with the label

    Output:
        The labelled output is displayed in the output area of a cell
    """
    import sympy as syp
    label1 = r"\;".join(label.split())
    display(Math("${} {} {}$".format( syp.latex(label1),syp.latex('\\rightarrow'),syp.latex(value))))
