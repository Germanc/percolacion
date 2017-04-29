#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = np.loadtxt("kap_0.0022.txt")
slope, intercept, r, pvalue, stderr =  linregress(np.log(data[:3,1]),
                                                  np.log(data[:3,0]))
nu = 2+slope
x = np.log(data[:,1])
y = np.log(data[:,0])
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.plot(x, y,'ro')
b = np.polyfit(data[35:45,1], data[35:45,0], 0)
plt.plot(x[:4], x[:4]*slope+intercept, 'k')
print("Beta: ", np.log(b)/np.log(0.022))
plt.plot(x[10:90], np.ones(80)*np.log(b), 'g')
#plt.xscale('log')
#ax.set_xlabel("L")
#ax.set_ylabel(r"$\rho(L)")
#plt.savefig("kap.pdf")
#plt.show()
print("Nu: ", nu)

#plt.plot(np.log(data[:,1]), np.log(data[:,0]),'ro')
#plt.plot(np.log(data[:4,1]), np.log(data[:4,1])*slope+intercept, 'b')
#print(np.log(intercept)/(0.035))
#plt.show()
data = np.loadtxt("kap_0.0035.txt")
slope, intercept, r, pvalue, stderr =  linregress(np.log(data[:2,1]),
                                                  np.log(data[:2,0]))
nu = 2+slope
x = np.log(data[:,1])
y = np.log(data[:,0])
plt.plot(x, y,'bo')
b = np.polyfit(data[35:45,1], data[35:45,0], 0)
plt.plot(x[:4], x[:4]*slope+intercept, 'k')
print("Beta: ", np.log(b)/np.log(0.035))
print("Nu: ", nu)
plt.plot(x[10:90], np.ones(80)*np.log(b), 'g')
#plt.xscale('log')
ax.set_xlabel("L")
ax.set_ylabel(r"$\rho(L)$")
plt.savefig("kap.png")
plt.show()


