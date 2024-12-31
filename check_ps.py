import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

m = np.load('./data/ps.npy')
hp.gnomview(m)
plt.savefig('./fig/ps.png', dpi=300)
plt.show()

freq_list = [30,50,90,150,300]
for freq in freq_list:
    m = np.load(f'./data/{freq}.npy')
    hp.gnomview(m)
    plt.savefig(f'./fig/{freq}.png', dpi=300)
    plt.show()