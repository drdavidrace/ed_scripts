############################################################
# Purpose:  These routines are used repeatedly in DiffEq so they 
#   are introduced in class once and then just imported
############################################################
import numpy as np
import typing
import numbers
#
#  define helper functions
#
def hVal(start:float = None , end:float = None, N:int = None) -> float:
    """Computes the best approximation between evenly spaced points
    
    Arguments:
        start {float} -- The starting point for an interval
        end {float} -- The ending point for an interval
        N {int} -- the number of evenly sized intervals in [start, end]

    Returns:
        float -- The best estimate for size of the evenly sized intervals
        None -- If there is a problem with the inputs

    NOTE:
        If np.narrays are passed in, then the corresponding sizes are computed for
        all provided intervals
    """
    try:
        return (end - start)/float(N)
    except:
        return None
#
def computeN(start=None,end=None,h=None):
    '''
    Purpose:  Define a common way to compute the number of intervals from h
    
    Inputs:
        All inputs default to None; therefore, they all must be provided
        start:  The start x value
        end:  The end x value
        h:  The size of the intervals
        
    Output:
        N - The number of intervals
    '''
    try:
        return int(np.ceil(fabs((float(end) - float(start))/float(h))))
    except:
        return None
#
def xVals(start:float = None, end:float = None, N:int = None) -> np.ndarray:
    """Compute the endpoints for the evenly spaced intervals 
    
    Keyword Arguments:
        start {float} -- The starting point for an interval
        end {float} -- The ending point for an interval
        N {int} -- the number of evenly sized intervals in [start, end]
    
    Returns:
        np.ndarray -- The np.narray of the end points for the given number of 
            intervals in [start, end]
        None -- It there is a problem with the inputs

    """
    try:
        return np.linspace(start,end,N+1)
    except:
        return None