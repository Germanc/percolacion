#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import glob

gpat = 'ns_*.txt'
fnames = glob.glob(gpat)
tab = np.empty((len(fnames), 4))
tamanio = 32
tau = 1.84
pc = 0.592566
sigma = 36/91

rango = int(np.floor(0.12*(tamanio**2)))
base = int(np.floor(0.01*(tamanio**2)))
critico = np.loadtxt("ns_0.592.txt")
ns_c, s_c = np.histogram(critico, bins=rango, range=[0, rango])
s_c = s_c[base:rango]
ns_c = ns_c[base:rango]/(tamanio*tamanio*27000)

fz_50 = []
z_50 = []
fz_60 = []
z_60 = []
fz_70 = []
z_70 = []
fz_80 =[]
z_80 = []

fig, ax = plt.subplots(nrows = 1, ncols = 1)
ax.set_xlabel(r's')
ax.set_ylabel(r'f(z)')
for j, archivo in enumerate(fnames):
    p = float(archivo.split('_', 1)[1].split('.txt', 1)[0])
    data = np.loadtxt(archivo)
    ns,s = np.histogram(data, bins=rango, range=[0, rango])
    s = s[base:rango]
    ns = ns[base:rango]
    ns = ns/(tamanio*tamanio*27000)
    fz = ns/ns_c
    fz_50.append(fz[90])
    z = (s**sigma)*(p-pc)/pc
    z_50.append(z[90])
    fz_60.append(fz[100])
    z_60.append(z[100])
    fz_70.append(fz[110])
    z_70.append(z[110])
    fz_80.append(fz[80])
    z_80.append(z[80])

ax.plot(z_50, fz_50,'bo')
ax.plot(z_60, fz_60, 'ro')
ax.plot(z_70, fz_70, 'go')
ax.plot(z_80, fz_80, 'yo')
plt.savefig("fz_problema4.pdf")
plt.show()
