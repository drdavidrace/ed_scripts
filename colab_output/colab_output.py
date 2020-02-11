#!/usr/bin/env python3
from IPython.display import HTML, Math, Latex
import sympy as sp
import pkg_resources
__version__ = pkg_resources.require('ed_scripts')[0].version
def display_matrix(left_side = "A = ", input_sympy = None) -> None:
    display(HTML("<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=default'></script>"))
    enhance_left = left_side.replace(" ","\\,")
    latex_sentence = "{}{}".format(enhance_left, sp.latex(input_sympy,mode='plain'))
    full_sentence = "\\begin{multline*}  " + latex_sentence + " \\end{multline*}"
    display(Math(full_sentence))
    return None
#from IPython.display import display, Math, HTML
#import pkg_resources
#__version__ = pkg_resources.require('ed_scripts')[0].version

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
