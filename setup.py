import os
from distutils.extension import Extension
from distutils.core import setup
from Cython.Build import cythonize

# Get the include directory for C++ headers
include_dir = os.environ.get('CPLUS_INCLUDE_PATH', '/usr/include/c++/11/')

# Define extension module to be build
extensions = [
    Extension("sigmulib",
              sources=["interface.pyx"],
              include_dirs=[include_dir],
              extra_compile_args=["-fopenmp"],
              extra_link_args=["-fopenmp"],
              language="c++")
]

# Setup configuration
setup(
    ext_modules=cythonize(extensions)
)
