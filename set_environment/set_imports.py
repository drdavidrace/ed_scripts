#!/usr/bin/env python3
#  The main imports for the education Colaboratory environment
#  This is considered bad practice, but I want to keep the worksheet focused on the Math and Sciene
import torch
import sklearn
import seaborn
import matplotlib
import pandas
import sympy
import scipy
import numpy
import pprint
import in_array
import sys
import os
#  Short cuts
import torch as T
import sklearn as skl
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import sympy as sp
import scipy as scp
import numpy as np
from pprint import pprint
from in_array import in_array
import torch as T
#
def set_up_globals():
    print('Setting the Environment Libraries')
    global py_version, np_version, skl_version, pd_version, mpl_version, torch_version, in_array_version
    py_version = sys.version_info
    np_version = np.__version__
    skl_version = skl.__version__
    pd_version = pd.__version__
    mpl_version = mpl.__version__
    torch_version = T.__version__
    in_array_version = in_array.__version__
    #  Checks
    print("Python Major Version: {}".format(py_version.major))
    print("Python Minor Version: {}".format(py_version.minor))
    if (py_version.major < 3):
        print("This code required Python 3")
    elif (py_version.major > 3):
        print("This code was built with Python 3, but this may work since the major version is higher.")
    elif (py_version.minor < 6):
        print("This code was built with Python 3.6, but this may work.  You might want to upgrade to version 3.6 or higher.")
    else:
        print("This code should work.")
    # Information
    print("This code was built with numpy version 1.16, you are using {}".format(np_version))
    print("This code was built with Scikit Learn version 0.21, you are using {}".format(
        skl_version))
    print("This code was built with Pandas version 0.24, you are using {}".format(
        pd_version))
    print("This code was built with Matplotlib version 3.0, you are using {}".format(
        mpl_version))
    print("This code was built with PyTorch version:  {}".format(torch_version))
    print("This notebook uses in_array version: {}".format(in_array_version))
    print("Finished Setting the Environment Libraries") 
