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
#       NOTE:  Ordinarily the latex output will be converted to pdf for review at t
#   display_t - display to a terminal
#       NOTE:  This is not considered very good output, but rather just a "summary"
#       that is not very enticing.  When used with output to a terminal (vs Jupyter)
#       this should be coupled with output to latex that is then converted to pdf
#   display_j - display to jupyter (colab) using mathjax
#   display_header_j - Uses sp.pprint to display a text string
#   display_header_pj - Uses the latex to display a text string
#
#  Input Format:
#   The main input format will be a list of items to display on a line.  The output
#   is concatenated together with a space between to better display information.
#       NOTE:  The display_t only takes a single value for output.  This is often
#       in the form of an equation, so it is reasonable robust.
#
#  Main Libraries
#   sympy - sympy has a lot of flexibility for doing mathematics; therefore,
#   it is the foundation for most of the output.  It has a very powerful mathematics
#   management engine that does automatic converstion from math to latex.
##################################################################
#
from IPython.display import display, HTML, Math, Latex
from IPython import get_ipython
import typing
import numbers
#From sympy and numpy
import sympy
import numpy
import sympy as sp
import numpy as np
#From pandas
import pandas as pd
from pandas import DataFrame
from pprint import pprint, pformat
import importlib
from importlib.metadata import version
__version__ = version('ed_scripts')
#default numpy types
np_arrays = (np.ndarray)
#  sentence elements
_begin_mult_sentence_ = "\\begin{multline*}  "
_end_mult_sentence_ = " \\end{multline*}"
_mathjax_sentence_ = "<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.1/latest.js?config=default'></script>"
_jup_math_eq_delim_ = ""
_pdf_math_eq_delim_ = "$"
#default headder element
_header_element_ = "############################################################"
#Generic Type Definitions
from typing import TypeVar
term_type_set = {str, numbers.Number, sp.Basic, np_arrays}
TermType = TypeVar('TermType',str, numbers.Number, sp.Basic)
PrettyType = TypeVar('PrettyType',list, str, numbers.Number, sp.Basic)
# def _enable_sympy_in_cell_():
#     """Borrowed from colab.research.google.com

#         NOTE:  The hook_sympy_cells must run first
#     """
#     display(HTML(_mathjax_sentence_))

def _typeset_():
    """MathJax initialization for the current cell.
    
    This installs and configures MathJax for the current output.
    """
    display(HTML('''
        <script src="https://www.gstatic.com/external_hosted/mathjax/latest/MathJax.js?config=TeX-AMS_HTML-full,Safe&delayStartupUntil=configured"></script>
        <script>
            (() => {
            const mathjax = window.MathJax;
            mathjax.Hub.Config({
            'tex2jax': {
                'inlineMath': [['$', '$'], ['\\(', '\\)']],
                'displayMath': [['$$', '$$'], ['\\[', '\\]']],
                'processEscapes': true,
                'processEnvironments': true,
                'skipTags': ['script', 'noscript', 'style', 'textarea', 'code'],
                'displayAlign': 'center',
            },
            'HTML-CSS': {
                'styles': {'.MathJax_Display': {'margin': 0}},
                'linebreaks': {'automatic': true},
                // Disable to prevent OTF font loading, which aren't part of our
                // distribution.
                'imageFont': null,
            },
            'messageStyle': 'none'
            });
            mathjax.Hub.Configured();
        })();
        </script>
        '''))
#
def hook_sympy_cells():
    """Hook the mathjax to the cells before use

        NOTE:  
    """
    get_ipython().events.register('pre_run_cell', _typeset_)
#
def display_j(in_list: list = None) -> int:
    """This is a top level routine which displays output in Jupyter using mathjax
        NOTE:  This is currently only tested with Google Colaboratory
    
    Keyword Arguments:
        in_list {list} -- The list of stuff to display (default: {None})
    
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
        #Obtain the latex
        status, full_sentence = _display_l_(in_list,_jup_math_eq_delim_)
        #Use display(Math) to output the latex of the sympy expression to the output of a compute cell
        display(Math(full_sentence))
        return None
    except Exception as e:
        status = 2
        print("Something went amiss with the mathjax process.  Details: {}".format(e))
        return status
    return status
#
def display_header_j(in_val: str = None, include_top: bool = True, include_bot: bool = True) -> int:
    """Display a basic header (fundamentally a set of strings)
    
    Keyword Arguments:
        in_val {str} -- A string to display using sp.pprint (default: {None})
    
    Returns:
        int -- status
    """
    status = 0
    try:
        if in_val is None:
            sp.pprint(_header_element_)
        else:
            if include_top:
                sp.pprint(_header_element_)
            sp.pprint(in_val)
            if include_bot:
                sp.pprint(_header_element_)
        return None
    except:
        status = 1
        return status
def display_header_pj(in_val: str = None, include_top: bool = True, include_bot: bool = True) -> int:
    """Display a basic header (fundamentally a set of strings, but the input text is displayed using latex)
    
    Keyword Arguments:
        in_val {str} -- A string to display using display (default: {None})
    
    Returns:
        int -- status
    """
    status = 0
    try:
        if in_val is None:
            sp.pprint(_header_element_)
        else:
            if include_top:
                sp.pprint(_header_element_)
            status, full_sentence = _display_l_(in_val, _jup_math_eq_delim_)
            display(Math(full_sentence))
            if include_bot:
                sp.pprint(_header_element_)
        return None
    except:
        status = 1
        return status
#
def display_lp(in_list: list = None, f:typing.IO = None) -> int:
    """This is a top level routine which generates the output in latex to be converted to postscript
    
    Keyword Arguments:
        in_list {list} -- The list of stuff to display (default: {None})
        f {file-like object} -- The file to use for the display output (default: {None})
    
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
    #Test the output file
    try:
        assert hasattr(f,'write')  #Check if it is open for writing
    except:
        status = 2
        print("The input file must be an open file handle for writing.")
        return status
    #Main body of work
    try:
        #Obtain the latex
        status, full_sentence = _display_l_(in_list,_pdf_math_eq_delim_)
        f.write(full_sentence+"\n")
        return status
    except Exception as e:
        status = 4
        print("Something went amiss with the mathjax or write process.  Details: {}".format(e))
        return status
    return status
#
def display_t(in_val: TermType = None) -> (int, str):
    """This is a top level routine which generates the output in latex to be output to the terminal
    using sympy.pprint.  This only goes to stdout
    
    Keyword Arguments:
        left_side {list} -- The list of stuff to display (default: {None})
    
    Returns:
        int -- discription of the status
        str -- the latex string
    """
    status = 0
    try:
        assert in_val is not None
    except:
        status = 1
        print("The in_val must not be None.")
        return status, None
    work = None

    try:
        for v in term_type_set: 
            if isinstance(in_val, v):
                work = in_val
        if work is None:
            status = 1
            message = "The input must be of type: {}".format(term_type_set)
    except:
        status = 2
        message = "The input must be of type: {}".format(term_type_set)
        return status, message
    #Print the value to the terminal
    try:
        sp.pprint(work)
    except Exception as e:
        status = 4
        print("Something went amiss with the sympy.pprint process.  Details: {}".format(e))
        return status, None
    return status, None
#
#  Private routines
#
def _display_l_(in_list: list = None,eq_delim: str = _jup_math_eq_delim_) -> (int, str):
    """Create the output for latex version of output that is suitable for output that will be output to jupyter using mathjax

       Caveat:  It is assumed that the printing of the output to the file
       is handled separately from this function.
    
    Keyword Arguments:
        in_list {list} -- The list of items to display (default: {None})
        eq_delim {str} -- The delim for the begin and end of math equations.
            For display to jupyter -- ""
            For pdf -- pass in "$"
    
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
    status, message = _create_latex_sentence_(work, eq_delim)
    #Write the output
    if (status > 0) or (len(message) == 0):
        status = 2
        return status, message
    else:
        display_message = _begin_mult_sentence_ + message + _end_mult_sentence_
        return status, display_message
#
def _create_latex_sentence_(input_val: list = None, eq_delim: str = _jup_math_eq_delim_) -> (int, str):
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
            # w = v.replace(" ","\\,")
            out_str += ("\\," + v + "\\,")
        elif isinstance(v,numbers.Number):  #This works for numpy numbers also
            out_str += ("\\,{}\\,".format(v))
        elif isinstance(v, np_arrays):
            x = sp.symbols('x')
            if v.ndim == 1:
                #shape an array so it prints out in a row vs column
                x_dim = v.shape[0]
                v = np.reshape(v,(1,x_dim))
            x = sp.Matrix(v)
            out_str += (" " + eq_delim + sp.latex(x,mode='plain') + eq_delim)
        elif isinstance(v, tuple) or isinstance(v,list) or isinstance(v,dict) or isinstance(v,set):
            x = sp.symbols('x')
            x = v
            out_str += (" " + eq_delim + sp.latex(x,mode='plain') + eq_delim)
        else:
            try:
                assert v.has(sp.Basic)
                out_str += (" "+ eq_delim + sp.latex(v,mode='plain',mul_symbol="dot") + eq_delim)
            except:
                out_str += (" "+ eq_delim + sp.latex(v,mode='plain',mul_symbol="dot") + eq_delim)
    message = out_str
    return status, message
#
def display_table_j(vals:list = None, headings: list = None,title:str ='Data Table',start_row:int = 0, num_rows:int = 25):
    '''
    Purpose:
        Display a table of values in a nice graph format using panda
        
    Inputs:
        vals - a list of vectors of values to display
        headings - a list of string to use for titles of the table columns
        title - A title for the display table
        start_row - indicates where to start the table row.  Sometimes the interesting data isn't at the first value
        num_rows {int} -- The number of rows to display
    '''
    status = 0
    #Build the data 
    dta = {}
    num_cols = len(vals)
    num_vals = vals[0].size
    num_titles = len(headings)
    if num_cols != num_titles:
        return None
    try:
        for i in range(num_cols):
            dta[headings[i]] = vals[i]
        cols=headings
        pData = DataFrame(dta)
        pData = pData[cols]
        display(HTML('<b>'+title+'</b>'))
        if start_row + num_rows > num_vals:
            display(HTML(pData[-num_rows:].to_html()))
        else:
            display(HTML(pData[start_row:start_row + num_rows].to_html()))
    except:
        return None
#
#  Old stuff to remove later
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
