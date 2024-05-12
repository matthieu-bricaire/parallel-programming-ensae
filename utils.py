import torch.nn.functional as F
import torch
import time
import numpy as np

# Import sigmul functions from the custom extension
from sigmulib import compute_sigmul_cpp, compute_sigmul_cython


# Function to compute sigmul in a sequential way, using NumPy
def unparallel_sigmul(A):
    B = np.empty_like(A, dtype=np.float32)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            a = A[i, j]
            B[i, j] = a / (1 + np.exp(-a))
    return B


# Reference implementation of sigmul, using PyTorch
def sigmul_torch(A):
    sigm = F.sigmoid(A)
    res = A * sigm
    return res


# Function to compute sigmul with Cython, including the PyTorch -> C++ -> PyTorch type conversions
def sigmul_from_tensor_cython(A):
    An = np.asarray(A, dtype=np.float32)
    B = compute_sigmul_cython(An)
    return torch.tensor(B)


# Function to compute the average execution time of a given function
def compute_time(A, sigmul_fun, n_rep):
    start = time.time()
    for _ in range(n_rep):
        _ = sigmul_fun(A)
    return (time.time() - start) / n_rep


# Function to compare the execution times of the different sigmul implementations
def compare_times(A, n_rep=50,
                  include_cpp=True, include_conv_cython=False, include_sequential=False):

    times = {}

    # C++ based version
    if include_cpp:
        Al = A.tolist()
        times['sigmul_cpp'] = compute_time(Al, compute_sigmul_cpp, n_rep)

    # Naive version
    if include_sequential:
        times['sigmul_sequential'] = compute_time(A, unparallel_sigmul, n_rep)

    # Full cython version with type conversion
    if include_conv_cython:
        times['sigmul_cython_conversions'] = compute_time(A, sigmul_from_tensor_cython, n_rep)

    # Full cython version
    An = np.asarray(A, dtype=np.float32)
    times['sigmul_cython'] = compute_time(An, compute_sigmul_cython, n_rep)

    # Torch based version
    times['sigmul_torch'] = compute_time(A, sigmul_torch, n_rep)

    return times
