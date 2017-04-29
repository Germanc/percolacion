#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import glob
from scipy.signal import  savgol_filter

tamanio = 128
tau = 1.84
pc = 0.592
sigma = 36/91

fig, ax = plt.subplots(nrows = 1, ncols = 1)
ax.set_xlabel(r's')
ax.set_ylabel(r'f(z)')

data = np.loadtxt("distribucion_m2_200048065.txt")
#data = np.loadtxt("temporal")
probabilidad = data[:,0]
m2 = data[:,1]

#ordeno = np.argsort(probabilidad)
#probabilidad = probabilidad[ordeno]
#m2 = m2[ordeno]
#m2 = savgol_filter(m2,15,5)

#slope, intercept, r_value, p_value, std_err = linregress(s_guardar_log, p_max_log)

plt.plot(probabilidad, m2, 'bo')
plt.show()
indice = np.argmax(m2)
pc_p = probabilidad[indice]
f = 0.000
mascara1 = (probabilidad>(pc_p+f)) # lado derecho
mascara2 = (probabilidad<(pc_p-f)) # lado izquierdo

probabilidad1 = np.log(probabilidad[mascara1]-pc_p)
probabilidad2 = np.log(-probabilidad[mascara2]+pc_p)
m21 = np.log(m2[mascara1])
m22 = np.log(m2[mascara2])

#izquierda
emesi = []
pesi = []
emesd = []
pesd = []
prob1 = probabilidad[mascara1]-pc_p
prob2 = -probabilidad[mascara2]+pc_p
indice1 = np.argsort(prob1)
prob1 = prob1[indice1]
indice2 = np.argsort(prob2)
prob2 = prob2[indice2]
probabilidad1 = probabilidad1[indice1]
probabilidad2 = probabilidad2[indice2]
m21 = m21[indice1]
m22 = m22[indice2]

n=4 # numero de puntos para el ajuste lineal
for i in range(1,(np.size(probabilidad1))):
    maximo = np.min((np.size(probabilidad1), i+n))
    print(maximo)
    m, b = np.polyfit(probabilidad1[i:maximo], m21[i:maximo],1)
    emesi.append(-m)
    pesi.append(prob1[i])

for i in range(1,(np.size(probabilidad2))):
    maximo = np.min((np.size(probabilidad2), i+n))
    m, b = np.polyfit(probabilidad2[i:maximo], m22[i:maximo],1)
    emesd.append(-1/m)
    pesd.append(prob2[i])

plt.plot(pesi, emesi, 'r')
plt.plot(pesi, emesi, 'ro')
plt.plot(pesd, emesd, 'b')
plt.plot(pesd, emesd, 'bx')
plt.show()
#
#derivada1 = np.diff(m21)/np.diff(probabilidad1)
#derivada2 = np.diff(m22)/np.diff(probabilidad2)
#
#probabilidad1_d = (probabilidad1[1:]+probabilidad1[:-1])/2.
#probabilidad2_d = (probabilidad2[1:]+probabilidad2[:-1])/2.
#
##pendiente1,b1=np.polyfit(probabilidad1_d, derivada1, 1)
##pendiente2,b2=np.polyfit(probabilidad2_d, derivada2, 1)
##
##plt.plot(probabilidad1_d, probabilidad1_d*pendiente1+b1,'r')
##plt.plot(probabilidad2_d, probabilidad2_d*pendiente2+b2,'b')
#
#plt.plot(probabilidad1_d, derivada1, 'r', probabilidad2_d, derivada2, 'b')
#
#
#plt.show()

#codigo made by jose
#m3 = m2
#m3 = np.column_stack((probabilidad, m2))
#fig, ax = plt.subplots(nrows = 1, ncols = 1)
#n = np.argmax(m3[:, 1])
#print(m3[n, 1])
#X = m3[:, 0] - m3[n, 0]
#Y = m3[:, 1]
#
#f = 0.005
#
## Gama - :: Ordena los arrays.
#Xl = X[X < -f]
#Yl = Y[X < -f]
#
#ids = np.argsort(Yl)
#xl = Xl[ids]
#yl = Yl[ids]
#
## Gama +
#Xr = X[X > f]
#Yr = Y[X > f]
#
#ids = np.argsort(Yr)
#xr = Xr[ids]
#yr = Yr[ids]
#
## Toma distinta cantidad de puntos a izquierda y derecha.
#ll = xl.shape[0]
#lr = xr.shape[0]
#
#gama_l = np.empty((ll - 2, 2))
#gama_r = np.empty((lr - 2, 2))
#
#for n in range(2, ll):
#    res_l = linregress(np.log(-xl[ll - n:]), np.log(yl[ll - n:]))
#    gama_l[n - 2, :] = [ res_l[0], res_l[4] ]
#
#print("")
#for n in range(2, lr):
#    res_r = linregress(np.log(xr[lr - n:]), np.log(yr[lr - n:]))
#    gama_r[n - 2, :] = [ res_r[0], res_r[4] ]
#
#
#ax.plot(m3[:, 0], m3[:,1], 'o')
#
#ax.cla()
#
#ln = np.min([ ll, lr ]) - 2
#n = np.arange(ln)
#
#ax.errorbar(n, -1/gama_l[:ln, 0], yerr = gama_l[:ln, 1], fmt = 'o')
#ax.errorbar(n, -gama_r[:ln, 0], yerr = gama_r[:ln, 1], fmt = 's')
#plt.show()
