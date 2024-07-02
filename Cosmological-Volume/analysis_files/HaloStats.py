#Simple implementation of a halo mass function with error estimation based on https://pynbody.github.io/pynbody/_modules/pynbody/analysis/hmf.html
import numpy as np
from scipy.stats import binned_statistic

def halo_MF(halo_masses, log_M_min=8.0, log_M_max=15.0, delta_log_M=0.1, boxsize = 30):
	nbins = int(1 + (log_M_max - log_M_min)/delta_log_M)
	bins = np.logspace(log_M_min, log_M_max, num=nbins, base=10)
	bin_centers = (bins[:-1] + bins[1:]) / 2

	num_halos = np.histogram(halo_masses, bins)[0]
	normalisation = boxsize**3 * delta_log_M
	err = np.sqrt(num_halos) / normalisation
	num_halos = num_halos  / normalisation

	return bin_centers, num_halos, err
