#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import glob
from scipy.signal import  savgol_filter

gpat = 'ns_*.txt'
fnames = glob.glob(gpat)
tab = np.empty((len(fnames), 4))
#valor elegido para que el maximo este bien ubicado
tamanio = 128
rango = tamanio**2
base = 1

cantidad = rango-base
probabilidad = np.empty((len(fnames)))
m2 = np.empty((len(fnames)))


for j, archivo in enumerate(fnames):
    p = float(archivo.split('_', 1)[1].split('.txt', 1)[0])
    p_str = archivo.split('_', 1)[1].split('.txt', 1)[0]
    print(p_str)
    percolante = np.loadtxt("percolante_"+p_str+".txt")
    data = np.loadtxt(archivo)
    mascara = np.in1d(data, percolante)
    data = data[mascara]
    nombre = "nssinpercolante_"+p_str
    ns,s = np.histogram(data, bins=rango, range=[0, rango])
    s = s[base:rango]
    ns = ns[base:rango]
    ns = ns/(tamanio*tamanio*27000)
    np.savez(nombre, s, ns)

