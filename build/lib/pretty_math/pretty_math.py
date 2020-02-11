#!/usr/bin/env python3
from IPython.display import HTML, Math, Latex
import sympy as sp
import pkg_resources
__version__ = pkg_resources.require('ed_scripts')[0].version
#
#  Routines for displaying information in either a Colaboratory notebook or in a .tex file that will be converted to 
#  a pdf file for viewing
#
def display_sympy(left_side = "A = ", input_sympy = None) -> None:
    """This routine displays a matrix in Colab from a code cell
    
    Keyword Arguments:
        left_side {str} -- Defines a simple left side for the output (default: {"A = "})
        input_sympy {A sympy object} -- Uses sympy to get the latex version of the sympy statement (default: {None})
    
    Returns:
        [type] -- [description]
    """
    assert input_sympy is not None
    print(input_sympy.__class__)
    print(isinstance(input_sympy,tuple(sympy.core.all_classes)))
    display(HTML("<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=default'></script>"))
    enhance_left = left_side.replace(" ","\\,")
    latex_sentence = "{}{}".format(enhance_left, sp.latex(input_sympy,mode='plain'))
    full_sentence = "\\begin{multline*}  " + latex_sentence + " \\end{multline*}"
    #Use display(Math) to output the sympy expression to the output of a compute cell
    display(Math(full_sentence))
    return None

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
