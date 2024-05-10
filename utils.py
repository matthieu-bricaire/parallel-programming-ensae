import time
import torch
import torch.functional as F
from sigmulib import compute_sigmul

torch.manual_seed(29)


def sigmul_from_tensor(A):
    Al = A.tolist()
    B = compute_sigmul(Al)
    return torch.tensor(B)


def sigmul_torch(A):
    sigm = F.sigmoid(A)
    return sigm * A


def compute_time(A, sigmul_fun, n_rep):
    start = time.now()
    for _ in n_rep:
        B = sigmul_fun(A)
    return (time.now() - start)/n_rep


def compare_times(A, n_rep=50):
    times = {}

    #With sigmul from list
    Al = A.tolist()
    times['list'] = compute_time(Al, compute_sigmul, n_rep)

    #With sigmul from tensor
    times['tensor_1'] = compute_time(A, compute_sigmul, n_rep)

    #With sigmul from tensor - convert to list and back to tensor
    times['tensor_2'] = compute_time(A, sigmul_from_tensor, n_rep)

    #With sigmul from tensor - convert back to tensor
    times['tensor_3'] = compute_time(A, lambda x: torch.tensor(compute_sigmul(x)), n_rep)

    #With torch
    times['torch'] = compute_time(A, sigmul_torch, n_rep)

    return times
