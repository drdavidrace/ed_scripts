#
#
import sys, os
import numpy as np  
import scipy as scp
import sympy as sp
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb
import sklearn as skl
import torch as T
from in_array import in_array
import importlib
from importlib.metadata import version
__version__ = version('ed_scripts')
#
def show_environment():
    print('Showing the environment setup --')
    #  Checks
    print("Python Major Version: {}".format(sys.version_info.major))
    print("Python Minor Version: {}".format(sys.version_info.minor))
    if (sys.version_info.major < 3):
        print("This code required Python 3")
    elif (sys.version_info.major > 3):
        print("This code was built with Python 3, but this may work since the major version is higher.")
    elif (sys.version_info.minor < 6):
        print("This code was built with Python 3.6, but this may work.  You might want to upgrade to version 3.6 or higher.")
    else:
        print("This code should work.")
    # Information
    print("This code uses numpy version: {}".format(np.__version__))
    print("This code uses scipy version: {}".format(scp.__version__))
    print("This code uses sympy version: {}".format(sp.__version__))
    print("This code uses Scikit Learn version: {}".format(skl.__version__))
    print("This code uses Pandas version: {}".format(pd.__version__))
    print("This code uses Matplotlib version:{}".format(mpl.__version__))
    print("This code uses PyTorch version:  {}".format(T.__version__))
    print("This notebook uses in_array version: {}".format(in_array.__version__))
#
def set_up_gpu(in_use_double = True):
    use_double = in_use_double
    device = None
    float_dtype = None
    int_dtype = None
    if T.cuda.is_available():
        device = 'cuda' if T.cuda.is_available() else 'cpu'
        float_dtype = T.double if use_double else T.float
        int_dtype = T.long if use_double else T.int
        #Basic PyTorch Information

        print("The PyTorch device: {}".format(device))
        print("The PyTroch float dtype: {}".format(float_dtype))
        print("The PyTorch int dtype: {}".format(int_dtype))
        #Set the default types
        if T.cuda.is_available():
            T.cuda.device(device=device)
        T.set_default_dtype(float_dtype)
        print("Verifying the default dtype is 64 bit: {}".format(T.get_default_dtype()))
        print("Verifying the default device: {}".format(T.cuda.current_device()))
        return True, device, float_dtype, int_dtype
    else:
        print("The environment is not using a gpu.")
        return False, device, float_dtype, int_dtype

