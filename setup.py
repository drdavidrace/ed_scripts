from distutils.core import setup
'''
Setup for ed_scripts
'''
import os
from setuptools import setup

def read(fname):
      return open(os.path.join(os.path.dirname(__file__),fname)).read()

setup(name='ed_scripts',
      version='0.1',
      author='Dr David Race',
      author_email='dr.david.race@gmail.com',
      url='git+https://github.com/drdavidrace/ed_scripts.git',
      description=('routines to convert Colaboratory forms input strings to arrays of floats or ints'),
      long_description=read('README.md'),
      license='GNU General Public License',
      packages=['in_array','tests'],
      install_requires=['numpy','sympy'],
      test_suite='tests',
      zip_safe=False
     )