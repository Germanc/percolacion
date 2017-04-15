#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import glob

gpat = 'percolante_*.txt'
fnames = glob.glob(gpat)
lista = np.empty((len(fnames), 2))
iteraciones = 27000

for j, archivo in enumerate(fnames):
    data = np.loadtxt(archivo)
    L = float(archivo.split('_',1)[1].split('.txt',1)[0])
    data = np.sum(data)/(iteraciones)
    data = np.log(data)
    L = np.log(L)
    lista[j, :] = [L, data]

slope, intercept, r, pvalue, stderr = linregress(lista[:,0], lista[:,1])
fig, ax = plt.subplots(nrows = 1, ncols = 1)
ax.plot(lista[:,0], lista[:,1], 'ro')
ax.set_xlabel(r'Tamaño $log(L)$')
ax.set_ylabel(r'Densidad $log(M)$')
plt.savefig("masa_l.pdf")
print(slope)
plt.show()
