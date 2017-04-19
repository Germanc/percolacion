#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import glob

gpat = 'percolante_*.txt'
fnames = glob.glob(gpat)
lista = np.empty((len(fnames), 2))
tamanio = 32
iteraciones = 27000
pc = 0.5888
for j, archivo in enumerate(fnames):
    data = np.loadtxt(archivo)
    print(archivo)
    data = np.sum(data)/(iteraciones*tamanio*tamanio)
    p = float(archivo.split('_',1)[1].split('.txt',1)[0])
    lista[j, :] = [p, data]
fig, ax = plt.subplots(nrows = 1, ncols = 1)
ax.plot(lista[:,0], lista[:,1], 'ro')
ax.set_xlabel(r'Probabilidad $p$')
ax.set_ylabel(r'$P_\infty$')
plt.savefig("pinfinito.pdf")
plt.show()

mascara = np.empty(lista.shape, dtype=bool)
mascara[:,:] = (lista[:,0] < pc)[:,np.newaxis]
nueva_lista = np.ma.array(lista, mask=mascara)
nueva_lista = np.sort(nueva_lista, axis=0)
para_ajuste = nueva_lista[0:6,:]-[pc,0]
slope, intercept, r, pvalue, stderr = linregress(np.log(para_ajuste))
print(slope)

