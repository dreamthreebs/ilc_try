import numpy as np
import matplotlib.pyplot as plt
import healpy as hp

def pixel_ilc(sim):
    n_freq = len(sim)
    C = np.zeros((n_freq, n_freq))
    C = np.cov(sim)
    A = np.zeros((n_freq+1, n_freq+1))
    A[0:-1,0:-1] = 2 * C
    A[-1,0:n_freq] = 1
    A[0:n_freq,-1] = -1
    print(f'{A = }')
    b = np.zeros(n_freq+1)
    b[-1] = 1
    print(f'{b = }')
    x = np.linalg.solve(A, b)

    weight = x[0:n_freq]
    print(f'{weight = }')

    ilc = weight @ sim
    return weight, ilc