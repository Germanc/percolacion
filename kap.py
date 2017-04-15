#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = np.loadtxt("kap.txt")
slope, intercept, r, pvalue, stderr =  linregress(np.log(data[:4,1]),
                                                  np.log(data[:4,0]))
nu = 2+slope
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.plot(data[:,1], data[:,0],'ro')
plt.xscale('log')
ax.set_xlabel("L")
ax.set_ylabel(r"$\rho(L)")
plt.savefig("kap.pdf")
plt.show()
print(nu)

