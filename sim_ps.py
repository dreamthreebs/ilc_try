import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

nside = 1024
npix = hp.nside2npix(nside=nside)
beam = 30

def calculate_flux_at_frequency(freq: float, freq_ref: float, alpha: float, S0: float) -> float:
    """
    Calculate the flux density at a specific frequency using a power-law spectrum.
    
    :param freq: Frequency at which to calculate the flux (GHz)
    :param freq_ref: Reference frequency (GHz)
    :param alpha: Power-law spectral index
    :param S0: Flux density at the reference frequency (arbitrary units, e.g., Jy)
    :return: Flux density at the specified frequency
    """
    return S0 * (freq / freq_ref) ** (-alpha)

# Parameters
freq_ref = 30  # Reference frequency (GHz)
S0 = 10000.0  # Flux density at the reference frequency (Jy)
alpha = 1.5  # Power-law spectral index

m = np.zeros(npix)

freq_list = [30,50,90,150,300]
for freq in freq_list:
    print(f'{freq=}')
    freq_to_calculate = freq  # Frequency where flux is needed (GHz)
    flux = calculate_flux_at_frequency(freq_to_calculate, freq_ref, alpha, S0)
    pix_idx = hp.ang2pix(nside=nside, theta=0, phi=0, lonlat=True)
    m[pix_idx] = flux

    sm = hp.smoothing(m, fwhm=np.deg2rad(beam)/60)
    np.save(f'./data/{freq}.npy', sm)
