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
pc = 0.592
sigma = 36/91
#valor elegido para que el maximo este bien ubicado
rango = int(np.floor(0.44*(tamanio**2))) 
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

#slope, intercept, r_value, p_value, std_err = linregress(s_guardar_log, p_max_log)

mascara1 = (probabilidad>pc) # lado derecho
mascara2 = (probabilidad<pc) # lado izquierdo

probabilidad1 = np.log(probabilidad[mascara1]-pc)
probabilidad2 = np.log(-probabilidad[mascara2]+pc)
m21 = np.log(m2[mascara1])
m22 = np.log(m2[mascara2])

derivada1 = np.diff(m21)/np.diff(probabilidad1)
derivada2 = np.diff(m22)/np.diff(probabilidad2)

probabilidad1_d = (probabilidad1[1:]+probabilidad1[:-1])/2.
probabilidad2_d = (probabilidad2[1:]+probabilidad2[:-1])/2.

pendiente1,b1=np.polyfit(probabilidad1_d, derivada1, 1)
pendiente2,b2=np.polyfit(probabilidad2_d, derivada2, 1)

plt.plot(probabilidad1_d, probabilidad1_d*pendiente1+b1,'r')
plt.plot(probabilidad2_d, probabilidad2_d*pendiente2+b2,'b')



plt.show()



#codigo made by jose
m3 = m2
m2 = np.column_stack((probabilidad, m2))
fig, ax = plt.subplots(nrows = 1, ncols = 1)
n = np.argmax(m2[:, 1])
print(m2[n, 1])
X = m2[:, 0] - m2[n, 0]
Y = m2[:, 1]

f = 0.030

# Gama - :: Ordena los arrays.
Xl = X[X < -f]
Yl = Y[X < -f]

ids = np.argsort(Yl)
xl = Xl[ids]
yl = Yl[ids]

# Gama +
Xr = X[X > f]
Yr = Y[X > f]

ids = np.argsort(Yr)
xr = Xr[ids]
yr = Yr[ids]

# Toma distinta cantidad de puntos a izquierda y derecha.
ll = xl.shape[0]
lr = xr.shape[0]

gama_l = np.empty((ll - 2, 2))
gama_r = np.empty((lr - 2, 2))

for n in range(2, ll):
    res_l = linregress(np.log(-xl[ll - n:]), np.log(yl[ll - n:]))
    gama_l[n - 2, :] = [ res_l[0], res_l[4] ]

print("")
for n in range(2, lr):
    res_r = linregress(np.log(xr[lr - n:]), np.log(yr[lr - n:]))
    gama_r[n - 2, :] = [ res_r[0], res_r[4] ]


ax.plot(m2[:, 0], m2[:,1], 'o')

ax.cla()

ln = np.min([ ll, lr ]) - 2
n = np.arange(ln)

ax.errorbar(n, -gama_l[:ln, 0], yerr = gama_l[:ln, 1], fmt = 'o')
ax.errorbar(n, -gama_r[:ln, 0], yerr = gama_r[:ln, 1], fmt = 's')
plt.show()
