from IPython.display import display, Math, HTML
import pkg_resources
__version__ = pkg_resources.require('ed_scripts')[0].version

# def load_mathjax_in_cell_output():
#     """
#     Purpose:  Set up the Colaboratory compute cell to use mathjax display latex

#     Input:  None

#     Output None
#     """
#     display(HTML("<script src='https://www.gstatic.com/external_hosted/"
#                 "mathjax/latest/MathJax.js?config=default'></script>"))
               


def matheq_show(left, right):
    """
    Purpose:  Display the left and right side of an equation in a compute cell
    
    Arguments:
        left {type: str} -- A string containing the left side  of the equation in latex
        right {type:string} -- A string containing the right side of the equation in latex

    Output:
        The equation is displayed in the output area of a cell
    """
    display(Math("${} = {}$".format( latex(left),latex(right))))

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
    label1 = "\;".join(label.split())
    display(Math("${} {} {}$".format( latex(label1),latex('\\rightarrow'),latex(value))))