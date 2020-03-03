# ed_scripts

This contains basic scripts that are used within my educational notebooks.  The educational notebooks make extensive use of numpy, scipy and sympy, so these routines are a basis for most of the data input formatting.  The basic capabilities are summarized below:

## Input Array Rows

The six main funcations are :

* in_array.array_floats_np - This takes a string _(i.e. from param form using string or raw)_ or iterable and checks that the values can be converted to floats.  If not, it returns a **None** for the data; otherwise, a numpy array _(tensor)_ of the correct shape.  See the code for the details.

* in_array.array_floats_syp - This takes a string _(i.e. from param form using string or raw)_ or iterable and checks that the values can be converted to floats.  If not, it returns a **None** for the data; otherwise, a sympy array _(tensor)_ of the correct shape.  See the code for the details.

* in_array.matrix_floats_syp - This takes a string _(i.e. from param form using string or raw)_ or iterable and checks that the values can be converted to floats.  If not, it returns a **None** for the data; otherwise, a sympy matrix of the correct shape.  If the input does not meet the shape requirements for a sympy.Matrix, then it returns **None**.  See the code for the details.

* in_array.array_ints_np - This takes a string _(i.e. from param form using string or raw)_ or iterable and checks that the values can be converted to int.  If not, it returns a **None** for the data; otherwise, a numpy array _(tensor)_ of ints.  See the code for the details.

* in_array.array_ints_syp - This takes a string _(i.e. from param form using string or raw)_ or iterable and checks that the values can be converted to int.  If not, it returns a **None** for the data; otherwise, a sympy array _(tensor)_ of ints.  See the code for the details.

* in_array.matrix_ints_syp - This takes a string _(i.e. from param form using string or raw)_ or iterable and checks that the values can be converted to int.  If not, it returns a **None** for the data; otherwise, a sympy matrix of the correct shape.  If the input does not meet the shape requirements for a sympy.Matrix, then it returns **None**.  See the code for the details.

### Notes

>* It is preferred to use _raw_ input with comma seperated values.  The _raw_ input fails without the commas, but it is a much more natural way to input the values.

## Pretty Displays

Mathematics has an elegant language; however, it is not particularily conducive to display in a terminal.  With the need for better display, this package provides some basic display capabilities for Jupyter/Colaboratory, Latex/pdf, and terminal output.  The basic functions for these packages are summarized in the following paragraphs.

### Jupyter/Colaboratory Display

These functions work with Jupyter/Colaboratory in conjunction with MathJax to display rather complex mathematics.  

**NOTE:**  _There is a general incompatability between graphics output (matplotlib and bokeh) and the pretty display of comments, mathematics and data.  There is no current fix; therefore, the work-around is having separate output cells for these types of outputs.  This is no real handicap and probably makes the output more readable by having the separate functionality._

The primary functions:

#### display_header_j(str)

This displays a standard header on the output to help keep the python code small.  The input string is optional.

#### display_j(list)

This uses mathjax to display a complex list of values that are output.  The values can be sympy expressions, strings, numbers, or numpy arrays.  This is the primary way the nicer mathematics is displayed in Jupyter or Colaboratory.  

#### display_table_j(<parameters>)

This uses mathjax to display a table of values.  The output is attractive and easy to view for data.  The data input is assumed to be a list of data.  This keeps the input generic.  This uses Pandas for output.

>NOTE:  This is currently only tested with Colaboratory,.
