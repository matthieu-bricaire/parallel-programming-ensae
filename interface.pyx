from libcpp.vector cimport vector

ctypedef vector[float] FloatVector
ctypedef vector[FloatVector] my_matrix

cdef extern from "sigmul.cpp":
    # Declare the C++ function and types you want to use
    my_matrix sigmul(const my_matrix& A)

def compute_sigmul(my_matrix A):
    # Call the C++ function using the imported C++ interface
    cdef my_matrix B = sigmul(A)
    return B
