#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import glob
from scipy.signal import  savgol_filter

gpat = 'ns_*.txt'
fnames = glob.glob(gpat)
tab = np.empty((len(fnames), 4))
tamanio = 32
tau = 1.84
pc = 0.592566
sigma = 36/91
rango = int(np.floor(0.4*(tamanio**2)))
#base = int(np.floor(0.01*(tamanio**2)))
base = 1

cantidad = rango-base
probabilidad = np.empty((51))
m2 = np.empty((51))

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
    m2_p = np.sum(ns*(s**2))
    probabilidad[j] = p
    m2[j] = m2_p

#ax.plot(probabilidad, ns_p[:,9], 'bo')
#slope, intercept, r_value, p_value, std_err = linregress(s_guardar_log, p_max_log)



#plt.savefig(


#plt.savefig("fz_problema5.pdf")
#plt.show()
