from distutils.core import setup
'''
Setup for ed_scripts
'''
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='ed_scripts',
      version='0.6',
      author='Dr David Race',
      author_email='dr.david.race@gmail.com',
      url='git+https://github.com/drdavidrace/ed_scripts.git',
      description=(
          'routines to make using Colaboratory scripts easier for the classroom'),
      long_description=read('README.md'),
      license='GNU General Public License',
      packages=['in_array', 'pretty_math', 'diffe_math', 'tests'],
      install_requires=['numpy', 'scipy', 'sympy', 'pandas',
                        'matplotlib', 'seaborn', 'sklearn', 'torch','IPython'],
      test_suite='tests',
      zip_safe=False
      )
