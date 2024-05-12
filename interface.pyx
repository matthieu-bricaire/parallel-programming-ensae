from libcpp.vector cimport vector
from libc.math cimport exp

from cython.parallel import prange
import cython

import numpy as np

ctypedef vector[float] FloatVector
ctypedef vector[FloatVector] my_matrix

cdef extern from "sigmul.cpp":
    # Declare the C++ function and types you want to use
    my_matrix sigmul(const my_matrix& A)

def compute_sigmul_cpp(my_matrix A) -> my_matrix:
    # Call the C++ function using the imported C++ interface
    cdef my_matrix B = sigmul(A)
    return B

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

def compute_sigmul_cython(A):
    return sigmul_cython(A)
