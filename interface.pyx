from libcpp.vector cimport vector
from libc.math cimport exp

from cython.parallel import prange
import cython

import numpy as np


# Definition of types corresponding to a 2D float matrix
ctypedef vector[float] FloatVector
ctypedef vector[FloatVector] my_matrix


# Declaration of the sigmul function from its external source file
cdef extern from "sigmul.cpp":
    my_matrix sigmul(const my_matrix& A)


# Wrapper to expose the C++ version of the sigmul function to Python users
def compute_sigmul_cpp(my_matrix A) -> my_matrix:
    cdef my_matrix B = sigmul(A)
    return B


# Cython function to compute the sigmul operation
@cython.boundscheck(False)
cdef float[:, :] sigmul_cython(float[:, :] A):
    cdef int rows = A.shape[0]
    cdef int cols = A.shape[1]
    cdef float[:, :] B = np.empty_like(A) # A.copy()
    cdef int i, j
    cdef float a

    for i in prange(rows, nogil=True):
        for j in range(cols):
            a = A[i, j]
            B[i, j] = a / (1.0 + exp(-a))

    return B


# Wrapper to expose the Cython version of the sigmul function to Python users
def compute_sigmul_cython(A):
    return sigmul_cython(A)
