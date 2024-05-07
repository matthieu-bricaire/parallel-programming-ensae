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
    Extension("sigmulib", ["interface.pyx"],
              include_dirs=["/usr/include/c++/11/"],
              language="c++")
]

setup(
    ext_modules=cythonize(extensions)
)
