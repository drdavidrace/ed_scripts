from distutils.core import setup
'''
Setup for ed_scripts
'''
from setuptools import setup


setup(name='ed_scripts',
      version='0.0.1.a',
      author='Dr David Race',
      author_email='dr.david.race@gmail.com',
      url='git+https://github.com/drdavidrace/ed_scripts.git',
      description='routines to convert Colaboratory forms input strings to arrays of floats or ints',
      long_description=' ',
      license='GNU General Public License',
      packages=['in_array'],
      zip_safe=False
     )