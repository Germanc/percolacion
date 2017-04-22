#!/usr/bin/python3
import numpy as np
import matplotlib.pylab as plt
from scipy.stats import linregress

data = np.loadtxt("ns_128.txt")
y,x = np.histogram(data, bins=200, range=[0, 200])
x = x[:200]
x = np.log10(x)
y = np.log10(y)
mask = np.isfinite(x) & np.isfinite(y)
slope, intercept, r_value, p_value, std_err = linregress(x[mask], y[mask])
# Tengo errores de division por cero
# Hay que eliminar los ceros primero
# Puedo usar menos bins
# Ademas para el ajuste necesito quedarme solo
# con la parte lineal, eso hay que hacerlo a mano
plt.plot(x[mask], y[mask],'ro')
plt.plot(x[mask], slope*x[mask]+intercept, 'b')
plt.ylabel(r'$n_{s}(p_c)$ (log)')
plt.xlabel(r'Tamaño de cluster s (log)')
plt.savefig('nspctau.png')
print("Tau: ", -slope)
plt.show()
