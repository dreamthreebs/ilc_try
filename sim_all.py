import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

from pathlib import Path

cmb = np.load('./data/cmb.npy')
path_sim = Path('./data/sim')
path_sim.mkdir(exist_ok=True, parents=True)

freq_list = [30,50,90,150,300]
for freq in freq_list:
    print(f'{freq=}')
    ps = np.load(f'./data/{freq}.npy')
    sim = cmb + ps
    np.save(path_sim / Path(f'{freq}.npy'), sim)
