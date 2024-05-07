# from distutils.core import setup
# from distutils.extension import Extension
# from Cython.Build import cythonize

# extensions = [
#     Extension("mylib", ["example.pyx"],
#               include_dirs=["/usr/include/c++/11/"],
#               language="c++")
# ]

# setup(
#     ext_modules=cythonize(extensions)
# )

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension("sigmulib",
              sources=["interface.pyx", "sigmul.cpp"],
              include_dirs=["/usr/include/c++/11/"],
              extra_compile_args=["-fopenmp"],
              extra_link_args=["-fopenmp"],
              language="c++")
]

setup(
    ext_modules=cythonize(extensions)
)
