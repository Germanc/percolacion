#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import glob

gpat = 'percolacion_b_*.txt'
fnames = glob.glob(gpat)
tab = np.empty((len(fnames), 4))

for j, archivo in enumerate(fnames):
    data = np.loadtxt(archivo)
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.plot(data[:,0], data[:,1], 'ro')
    ax.set_xlabel('Probabilidad')
    ax.set_ylabel('F(p)')
    L = archivo.split("_b_")[1].split(".")[0]
    plt.savefig(L+".pdf")
    plt.show()
#    slope, intercept, r, pvalue, stderr = linregress(x, y)


