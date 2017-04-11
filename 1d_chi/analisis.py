#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import glob

gpat = 'ns_*.txt'
fnames = glob.glob(gpat)
tab = np.empty((len(fnames), 4))
tamanio = 32

for j, archivo in enumerate(fnames):
    data = np.loadtxt(archivo)
    y,x = np.histogram(data, bins=200,range=[0,200])
    x = x[:200]
    y = y/(tamanio*tamanio*27000)
    x = np.log(x)
    y = np.log(y)
    mask = np.isfinite(x) & np.isfinite(y)
    plt.show()
    slope, intercept, r, pvalue, stderr = linregress(x[mask], y[mask])
#    slope, intercept, r, pvalue, stderr = linregress(x, y)
    p = float(archivo.split('_',1)[1].split('.txt',1)[0])
    tab[j, :] = [r**2, p, slope, intercept]
    print(p, " ", r**2)

fig, ax = plt.subplots(nrows = 1, ncols = 1)
ax.plot(tab[:,1], tab[:,0], 'ro')
ax.set_xlabel(r'Probabilidad $p$')
ax.set_ylabel(r'$n_s(p)$')
plt.savefig("ns_p.pdf")
plt.show()
