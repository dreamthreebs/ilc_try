import numpy as np
import matplotlib.pyplot as plt

def generate_single_power_law_source(freq_min: float, freq_max: float, 
                                      alpha: float, S0: float, num_freqs: int = 100):
    """
    Generate flux density data for a single point source following a power-law spectrum.
    
    :param freq_min: Minimum frequency (in GHz)
    :param freq_max: Maximum frequency (in GHz)
    :param alpha: Power-law spectral index
    :param S0: Flux density at the reference frequency (freq_min)
    :param num_freqs: Number of frequency points to compute
    :return: Array of frequencies, Array of flux densities
    """
    # Generate log-spaced frequency points
    freqs = np.logspace(np.log10(freq_min), np.log10(freq_max), num_freqs)
    
    # Compute flux density at each frequency using the power-law formula
    fluxes = S0 * (freqs / freq_min) ** (-alpha)
    
    return freqs, fluxes

# Parameters
freq_min = 30  # GHz
freq_max = 300  # GHz
alpha = 1.5  # Power-law spectral index
S0 = 10.0  # Reference flux density at freq_min (arbitrary units, e.g., Jy)
num_freqs = 100

# Generate data
freqs, fluxes = generate_single_power_law_source(freq_min, freq_max, alpha, S0, num_freqs)

# Visualization
fig, ax = plt.subplots()
ax.plot(freqs, fluxes, label=f"α={alpha}, S0={S0} Jy")
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Frequency (GHz)')
ax.set_ylabel('Flux Density')
ax.set_title('Power-Law Spectrum of a Single Point Source')
ax.legend()
plt.savefig("./fig/flux.png",dpi=300)
plt.show()
