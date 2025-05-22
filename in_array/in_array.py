from functools import reduce
import re
import numpy as np
import sympy as syp
from pprint import pprint
# import pkg_resources
#__version__ = pkg_resources.require('ed_scripts')[0].version
import importlib
from importlib.metadata import version
__version__ = version('ed_scripts')

def matrix_float_syp(in_val=None):
	"""
	Purpose:  This takes in a string of floats
	
	Keyword Arguments:
		in_val {string or iterable} -- [attempts to build a matrix from the inputs] (default: {None})

	Returns
		sympy.Matrix if conversion is possible
		None otherwise
	"""
	assert in_val is not None
	res_syp = array_float_syp(in_val)
	if res_syp is None:
		return None
	else:
		try:
			return res_syp.tomatrix()
		except:
			return None

def array_float_syp(in_val=None):
	"""
	Purpose:  This takes input of a string of floats or interable and trys to convert it 
	
	Keyword Arguments:
		in_val {iterable or string} -- [attempts to build a tensor based upon the inputs]
	
	Returns:
		sympy.Array of if conversion is possible
		None otherwise
	"""
	assert in_val is not None
	res_np = array_float_np(in_val)
	if res_np is None:
		return None
	else:
		try:
			return syp.Array(res_np)
		except:
			return None

def array_float_np(in_val=None):
	"""
	Purpose:  This takes input of a string of floats or interable and trys to convert it 
	
	Keyword Arguments:
		in_val {iterable or string} -- attempts to build a tensor based upon the inputs
			This is type np.array since np.array allows multiple dimensions
	
	Returns:
		np.array of np.float64 if conversion is possible
		None otherwise
	"""
	assert in_val is not None
	in_data = None
	if isinstance(in_val, str):
		return(str_array_floats(in_val))
	else:
		try:
			in_data = [e for e in in_val]
			are_floats = _is_iter_float_(in_data)
			if are_floats:
				return np.array([float(t) for t in in_data])
		except TypeError:
			return None
	res_data = []
	for r in in_data:
		if isinstance(r,str):
			res = str_array_floats(r)
			res_data.append(res)
		else:
			rr = array_float_np(r)
			if rr is None or any( x is None for x in rr):
				res_data.append(None)
			else:
				res_data.append(array_float_np(r))
	if res_data is None or any(x is None for x in res_data):
		return None
	else:
		try:
			return np.array(res_data)
		except:
			return None

def str_array_floats(in_str=None):
	"""
	Purpose:  This takes in a string (typically from a colaboratory param) and attempts
	to convert it to an numpy array of floats.

	Inputs:
	in_str - The string to be converted to an array of floats

	Returns:
	ret_val :  	None if any value cannot be converted to a float
				Array of floats if all values can be converted to a float
	"""
	assert in_str is not None
	assert isinstance(in_str,str)
	row = re.split(r'[,\s]+',in_str)
	all_numbers = _str_check_floats_(row)
	if all_numbers:
		return np.array([float(r) for r in row])
	else:
		return None

def _is_float_(in_str=None):
  '''
  Purpose:  An internal routine just to check if a string can be converted to a float

  Input:  in_str - an input string

  Output:  True/False based upon the conversion
  '''
  assert in_str is not None
  ret_val = None
  try:
    float(in_str)
    ret_val = True
  except:
    ret_val = False
  return ret_val

def _is_iter_float_(in_iter=None):
	'''
	Purpose:  An internal routine just to check if a string can be converted to a float

	Input:  in_str - an input string

	Output:  True/False based upon the conversion
	'''
	assert in_iter is not None
	ret_val = None
	try:
		[float(t) for t in in_iter]
		ret_val = True
	except:
		ret_val = False
		pass
	return ret_val

def _str_check_floats_(row_vals=None):
	'''
	Purpose:  Internal routine to check each string in an array for valid floating point conversion
	
	Keyword Arguments:
		row_vals {string} -- [description] (default: {None})
	
	Returns:
		True if all values can be converted to float
		False if any value cannont be converted to float
	'''
	assert row_vals is not None
	check_numbers = [_is_float_(r) for r in row_vals]
	all_numbers = reduce(lambda x,y: x and y,check_numbers)
	return all_numbers
#
#  split integers
#
def matrix_int_syp(in_val=None):
	"""
	Purpose:  This takes in a string of floats
	
	Keyword Arguments:
		in_val {string or iterable} -- [attempts to build a matrix from the inputs] (default: {None})

	Returns
		sympy.Matrix if conversion is possible
		None otherwise
	"""
	assert in_val is not None
	res_syp = array_int_syp(in_val)
	if res_syp is None:
		return None
	else:
		try:
			return res_syp.tomatrix()
		except:
			return None

def array_int_syp(in_val=None):
	"""
	Purpose:  This takes input of a string of ints or interable and trys to convert it 
	
	Keyword Arguments:
		in_val {iterable or string} -- attempts to build a tensor based upon the inputs
	
	Returns:
		sympy.Tensor of if conversion is possible
		None otherwise
	"""
	assert in_val is not None
	res_np = array_int_np(in_val)
	if res_np is None:
		return None
	else:
		try:
			return syp.Array(res_np)
		except:
			return None

def array_int_np(in_val=None):
	"""
	Purpose:  This takes input of a string of ints or interable and trys to convert it 
	
	Keyword Arguments:
		in_val {iterable or string} -- attempts to build a tensor based upon the inputs
	
	Returns:
		np.array of np.int64 if conversion is possible
		None otherwise
	"""
	assert in_val is not None
	in_data = None
	if isinstance(in_val, str):
		return(str_array_ints(in_val))
	else:
		try:
			in_data = [e for e in in_val]
			is_iter_int = _is_iter_int_(in_data)
			if is_iter_int:
				return np.array([int(t) for t in in_data])
			elif (not is_iter_int) and (_is_convert_iter_int_(in_data)):
				return None
		except TypeError:
			return None
	res_data = []
	for r in in_data:
		if isinstance(r,str):
			res = str_array_ints(r)
			res_data.append(res)
		else:
			rr = array_int_np(r)
			if rr is None or any( x is None for x in rr):
				res_data.append(None)
			else:
				res_data.append(array_int_np(r))
	if res_data is None or any(x is None for x in res_data):
		return None
	else:
		try:
			return np.array(res_data)
		except:
			return None

def str_array_ints(in_str=None):
	assert in_str is not None
	assert isinstance(in_str,str)
	row = re.split(r'[,\s]+',in_str)
	all_numbers = _str_check_ints_(row)
	if all_numbers:
		return np.array([int(r) for r in row])
	else:
		return None

def _is_int_(in_str=None):
	'''
	Purpose:  Takes in a string and check if it can be converted to an int

	Keyword Arguments:
		in_str {string} -- the string to check for valid conversion (default: {None})
	
	Returns:
		True if the conversion is successful
		False otherwise
	'''

	assert in_str is not None
	assert isinstance(in_str,str)
	ret_val = None
	try:
		int(in_str)
		ret_val = True
	except:
		ret_val = False
	return ret_val

def _is_iter_int_(in_iter=None):
	'''
	Purpose:  Takes in a string and check if it can be converted to an int

	Keyword Arguments:
		in_str {string} -- the string to check for valid conversion (default: {None})
	
	Returns:
		True if the conversion is successful
		False otherwise
	'''

	assert in_iter is not None
	ret_val = None
	try:
		[int(t) for t in in_iter]
		ret_val = all([float(int(t)) == float(t) for t in in_iter])
	except:
		ret_val = False
	return ret_val

def _is_convert_iter_int_(in_iter=None):
	'''
	Purpose:  Takes in a string and check if it can be converted to an int

	Keyword Arguments:
		in_str {string} -- the string to check for valid conversion (default: {None})
	
	Returns:
		True if the conversion is successful
		False otherwise
	'''

	assert in_iter is not None
	ret_val = None
	try:
		[int(t) for t in in_iter]
		ret_val = True
	except:
		ret_val = False
	return ret_val

def _str_check_ints_(row_vals=None):
	'''
	Purpose:  Takes in an array of strings and checks them all for conversion to ints
	
	Keyword Arguments:
		row_vals {array of strings} -- [The strings to check for conversion to ints] (default: {None})
	
	Returns:
		True -  If all of the values can be converted to an int
		False -  Otherwise
	'''

	assert row_vals is not None
	check_numbers = [_is_int_(r) for r in row_vals]
	all_numbers = reduce(lambda x,y: x and y,check_numbers)
	return all_numbers
