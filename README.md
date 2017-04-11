# Percolacion

Implementación de la primera guía de Física Computacional 2017.

*percolacion.c*: En stdout devuelve [pc, sigma]. En ns.txt devuelve el tamaño de los clusters en todas las iteraciones. Es necesario normalizar y hacer un histograma de esos datos en python para calcular ns(pc). Los datos que devuelve es para los pc calculados, y no para cualquier p arbitrario. En ns_percolante.txt devuelve el tamaño de los clusters percolantes.

*percolacion_b.c*: Devuelve en percolacion_b.txt la función F(p)dp, correspondiente al item 1.b.

*hoshen.c*: Implementación del algoritmo de Hoshen-Kopelman.

*ns.c*: devuelve en el archivo ns.txt el tamaño de cada uno de los clusters de la red dada como input.

percolacion_d.c: Calcula ns(p) dado cierto p como parámetro. Devuelve ns.txt con los datos para realizar el histograma en python, con 1d/ns.py y devuelve en ns_percolante.txt el tamaño del cluster percolante.
