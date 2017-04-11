import pylab
import numpy

from io import StringIO

data = numpy.loadtxt("percolacion_d_datos.txt")

pylab.plot(data[:,0], data[:,1])