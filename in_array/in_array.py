from functools import reduce
import re

def array_floats(in_str=None):
  """
  Purpose:  This takes in a string (typically from a colaboratory param) and attempts
  to convert it to an array of floats.

  Inputs:
  in_str - The string to be converted to an array of floats

  Returns:
  ret_val :  None if any value cannot be converted to a float
              Array of floats if all values can be converted to a float
  comment: A simple comment that is primarily used for communicating status
  """
  assert in_str is not None
  assert isinstance(in_str,str)
  row = re.split(r'[,\s]+',in_str)
  all_numbers = _check_floats_(row)
  ret_val = None
  comment = None
  if all_numbers:
    ret_val = [float(r) for r in row]
    comment = 'The values are all floats'
  else:
    ret_val = None
    comment = 'The values are not all floats, please correct the values'
  return ret_val, comment

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

def _check_floats_(row_vals=None):
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
#  split integers (for using sympy)
#
def array_ints(in_str=None):
  assert in_str is not None
  row = re.split(r'[,\s]+',in_str)
  all_numbers = _check_ints_(row)
  ret_val = None
  comment = None
  if all_numbers:
    ret_val = [int(r) for r in row]
    comment = 'The values are all integers'
  else:
    ret_val = None
    comment = 'The values are not all integers, please correct the values'
  return ret_val, comment

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

def _check_ints_(row_vals=None):
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