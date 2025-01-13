import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

cls = np.load('./data/cmbcl_8k.npy').T[0]
print(f'{cls.shape=}')

nside = 1024
np.random.seed(0)
cmb = hp.synfast(cls, nside=nside)
np.save('data/cmb.npy', cmb)
hp.mollview(cmb)
plt.savefig('./fig/cmb.png', dpi=300)
