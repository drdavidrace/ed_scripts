# ed_scripts
This contains basic scripts that are used within my educational notebooks.  The educational notebooks make extensive use of numpy, scipy and sympy, so these routines are a basis for most of the data input formatting.  The basic capabilities are summarized below:

## Input Array Rows
The six main funcations are :

*  in_array.array_floats_np - This takes a string (i.e. from param form) or iterable and checks that the values can be converted to floats.  If not, it returns a **None** for the data; otherwise, a numpy array _(tensor)_ of the correct shape.  See the code for the details.

*  in_array.array_floats_syp - This takes a string (i.e. from param form) or iterable and checks that the values can be converted to floats.  If not, it returns a **None** for the data; otherwise, a sympy array _(tensor)_ of the correct shape.  See the code for the details.

*  in_array.matrix_floats_syp - This takes a string (i.e. from param form) or iterable and checks that the values can be converted to floats.  If not, it returns a **None** for the data; otherwise, a sympy matrix of the correct shape.  If the input does not meet the shape requirements for a sympy.Matrix, then it returns **None**.  See the code for the details.

*  in_array.array_ints_np - This takes a string (i.e. from param form) or iterable and checks that the values can be converted to int.  If not, it returns a **None** for the data; otherwise, a numpy array _(tensor)_ of ints.  See the code for the details.

*  in_array.array_ints_syp - This takes a string (i.e. from param form) or iterable and checks that the values can be converted to int.  If not, it returns a **None** for the data; otherwise, a sympy array _(tensor)_ of ints.  See the code for the details.

*  in_array.matrix_ints_syp - This takes a string (i.e. from param form) or iterable and checks that the values can be converted to int.  If not, it returns a **None** for the data; otherwise, a sympy matrix of the correct shape.  If the input does not meet the shape requirements for a sympy.Matrix, then it returns **None**.  See the code for the details.