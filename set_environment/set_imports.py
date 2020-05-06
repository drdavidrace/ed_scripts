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
#
import pkg_resources
__version__ = pkg_resources.require('ed_scripts')[0].version
#
def show_environment():
    print('Showing the environment setup --')
    #  Checks
    print("Python Major Version: {}".format(sys.version_info.major))
    print("Python Minor Version: {}".format(sys.version_info.minor))
    if (py_version.major < 3):
        print("This code required Python 3")
    elif (py_version.major > 3):
        print("This code was built with Python 3, but this may work since the major version is higher.")
    elif (py_version.minor < 6):
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
