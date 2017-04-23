#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

from pylab import rcParams
data1 = np.loadtxt("kap_0.0035.txt")
data2 = np.loadtxt("kap_0.0022.txt")
slope1, intercept1, r1, pvalue1, stderr1 =  linregress(np.log(data1[:4,1]),
                                                  np.log(data1[:4,0]))
slope2, intercept2, r2, pvalue2, stderr2 =  linregress(np.log(data2[:4,1]),
                                                  np.log(data2[:4,0]))

nu1 = 2+slope1
nu2 = 2+slope2
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.plot(data1[:,1], data1[:,0],'ro')
plt.plot(data2[:,1], data2[:,0],'bx')
plt.xscale('log')
plt.yscale('log')
ax.set_xlabel("L")
ax.set_ylabel(r"$\rho(L)$")
plt.savefig("kap.png")
plt.show()
print("Nu 1: ", nu1, "|| Nu 2: ", nu2)

