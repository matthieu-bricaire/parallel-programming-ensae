import time
import torch
import torch.nn.functional as F
from sigmulib import compute_sigmul_cpp, compute_sigmul_cython
import numpy as np

torch.manual_seed(29)


def sigmul_from_tensor_cython(A):
    An = np.asarray(A, dtype=np.float32)
    B = compute_sigmul_cython(An)
    return torch.tensor(B)


def sigmul_torch(A):
    sigm = F.sigmoid(A)
    res = A * sigm
    return res


def compute_time(A, sigmul_fun, n_rep):
    start = time.time()
    for _ in range(n_rep):
        _ = sigmul_fun(A)
    return (time.time() - start) / n_rep


def compare_times(A, n_rep=50, include_cpp=True, include_conv_cython=False):
    times = {}

    if include_cpp:
        # C++ based version
        Al = A.tolist()
        times['sigmul_cpp'] = compute_time(Al, compute_sigmul_cpp, n_rep)

    if include_conv_cython:
        times['sigmul_cython_with_conv'] = compute_time(A, sigmul_from_tensor_cython, n_rep)

    # Full cython version
    An = np.asarray(A, dtype=np.float32)
    times['sigmul_cython'] = compute_time(An, compute_sigmul_cython, n_rep)

    # Torch based version
    times['sigmul_torch'] = compute_time(A, sigmul_torch, n_rep)

    return times
