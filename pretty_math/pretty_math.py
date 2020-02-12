#!/usr/bin/env python3
from IPython.display import display, HTML, Math, Latex
import sympy
from sympy import *
import sympy as sp
import pkg_resources
__version__ = pkg_resources.require('ed_scripts')[0].version
#
#  Routines for displaying information in either a Colaboratory notebook or in a .tex file that will be converted to 
#  a pdf file for viewing
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
        assert input_sympy.has(Basic)
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
def display_sympy(left_side = None, input_sympy = None) -> int:
    """This routine displays a sympy element in Colab from a code cell
    
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
        assert input_sympy.has(Basic)
    except:
        status = 2
        print("The right side must be a sympy expression.")
        print("The right side type: {}".format(type(input_sympy)))
        return status
    #Main body of work
    try:
        display(HTML("<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=default'></script>"))
        # enhance_left = left_side.replace(" ","\\,")
        # latex_sentence = "{}{}".format(enhance_left, sp.latex(input_sympy,mode='plain'))
        # full_sentence = "\\begin{multline*}  " + latex_sentence + " \\end{multline*}"
        full_sentence = _get_latex_sympy_(left_side,input_sympy)
        #Use display(Math) to output the sympy expression to the output of a compute cell
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
