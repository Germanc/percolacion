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
rango = int(np.floor(0.12*(tamanio**2)))
base = int(np.floor(0.01*(tamanio**2)))

critico = np.loadtxt("ns_0.592.txt")
ns_c, s_c = np.histogram(critico, bins=rango, range=[0, rango])
s_c = s_c[base:rango]
ns_c = ns_c[base:rango]/(tamanio*tamanio*27000)
cantidad = rango-base
ns_p = np.empty((51, cantidad))
z_p = np.empty((51, cantidad))
fz_p = np.empty((51,cantidad))
probabilidad = np.empty((51))
fz_10 = []
z_10 = []

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
    z = (s**sigma)*(p-pc)/pc
    probabilidad[j] = p
    ns_p[j,:] = ns
    z_p[j,:] = z
    fz = ns/ns_c
    fz_p[j,:] = fz
    fz_10.append(fz[10])
    z_10.append(z[10])

#ax.plot(probabilidad, ns_p[:,9], 'bo')
s_guardar = []
p_max = []
for i in range(50, 110):
    datos = np.array([probabilidad, ns_p[:,i]])
    datos = np.transpose(datos)
    datos = datos[datos[:,0].argsort()]
    datos[:,1] = savgol_filter(datos[:,1],7,1)
    indice = np.argmax(datos[:,1])
    s_guardar.append(s[i])
    p_max.append(datos[indice,0])

s_guardar_log = np.array(np.log(s_guardar))
p_max = np.array(p_max)
p_max_log = np.log(pc-p_max)

slope, intercept, r_value, p_value, std_err = linregress(s_guardar_log,
                                                         p_max_log)
print("El valor de sigma es ", -slope)


#plt.savefig(


#plt.savefig("fz_problema5.pdf")
#plt.show()
