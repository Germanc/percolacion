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


#data = np.loadtxt("distribucion_m2.txt")
#data = np.loadtxt("distribucion_m2_30055064.txt")
data = np.loadtxt("distribucion_m2_200048065.txt")
data = np.loadtxt("temporal")
#data = np.loadtxt("distribucion_m2_L64.txt")
probabilidad = data[:,0]
m2 = data[:,1]

#ordeno = np.argsort(probabilidad)
#probabilidad = probabilidad[ordeno]
#m2 = m2[ordeno]
#m2 = savgol_filter(m2,15,5)

#slope, intercept, r_value, p_value, std_err = linregress(s_guardar_log, p_max_log)

plt.plot(probabilidad, m2, 'bo')
plt.xlabel(r'Probabilidad p')
plt.ylabel(r'$m_{2}(p)$')
plt.savefig('m2_p.png')
plt.show()
indice = np.argmax(m2)
pc_p = probabilidad[indice]
pc_p = 0.58
f = 0.015
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

n=6 # numero de puntos para el ajuste lineal
sp = 1
for i in range(sp,(np.size(probabilidad1))-n):
    maximo = np.min((np.size(probabilidad1), i+n))
    maximo = i+n
    print(maximo)
    m, b = np.polyfit(probabilidad1[i:maximo], m21[i:maximo],1)
    emesi.append(-m)
    pesi.append(prob1[i+int(np.floor(n/2))])

for i in range(sp,(np.size(probabilidad2)-n)):
    maximo = np.min((np.size(probabilidad2), i+n))
    maximo = i+n
    m, b = np.polyfit(probabilidad2[i:maximo], m22[i:maximo],1)
    emesd.append(-m)
    pesd.append(prob2[i+int(np.floor(n/2))])

inicio = 0
fin = 30
plt.plot(pesi[inicio:fin], emesi[inicio:fin], 'r')
plt.plot(pesi[inicio:fin], emesi[inicio:fin], 'ro')
plt.plot(pesd[inicio:fin], emesd[inicio:fin], 'b')
plt.plot(pesd[inicio:fin], emesd[inicio:fin], 'bx')
plt.xlabel(r'$|p-p_{c}|$')
plt.ylabel(r'$\gamma_{+}, \gamma_{-}$')
plt.savefig('gamma.png')
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
#
#
#n = np.argmax(m3[:, 1])
##pint('p_max {0}, max: {1}'.format(m2[n, 0], m2[n, 1]))
#
## Ordena los arrays.
#ids = np.argsort(m3[:, 1])
#
#X = m3[ids, 0] - m3[n, 0]
#Y = m3[ids, 1]
#
## Usa el Método Germán-Elliot.
#
#f = 0
#
#X_lft = X[X < -f]
#Y_lft = Y[X < -f]
#
#X_rgt = X[X > f]
#Y_rgt = Y[X > f]
#
#dl = 3
#
#max_lft = int(np.floor(X_lft.shape[0]/dl))
#max_rgt = int(np.floor(X_rgt.shape[0]/dl))
#gamma_lft = np.empty((max_lft, 2))
#gamma_rgt = np.empty((max_rgt, 2))
#
#dist = np.arange(max_lft)
#dist_a = np.arange(max_rgt)
#
#for n in dist:
#    res = linregress(np.log(-X_lft[n:n + dl]), np.log(Y_lft[n:n + dl]))
#    gamma_lft[n, :] = [ res[0], res[4] ]
#
#for n in dist_a:
#    res = linregress(np.log(X_rgt[n:n + dl]), np.log(Y_rgt[n:n + dl]))
#    gamma_rgt[n, :] = [ res[0], res[4] ]
#
##gamma_rgt[:,0] = savgol_filter(gamma_rgt[:,0], 11, 3)
##gamma_lft[:,0] = savgol_filter(gamma_lft[:,0], 11, 3)
#plt.plot(dist, -gamma_lft[:, 0], 'bo')
#plt.plot(dist, -gamma_lft[:, 0], 'b')
#plt.plot(dist_a, -gamma_rgt[:, 0], 'ro')
#plt.plot(dist_a, -gamma_rgt[:, 0], 'r')
#plt.show()
#
