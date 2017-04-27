# Percolacion

Implementación de la primera guía de Física Computacional 2017.

*percolacion.c*: En stdout devuelve [pc, sigma]. En ns.txt devuelve el tamaño de los clusters en todas las iteraciones. Es necesario normalizar y hacer un histograma de esos datos en python para calcular ns(pc). Los datos que devuelve es para los pc calculados, y no para cualquier p arbitrario. En ns_percolante.txt devuelve el tamaño de los clusters percolantes.

*percolacion_b.c*: Devuelve en percolacion_b.txt la función F(p)dp, correspondiente al item 1.b.

*hoshen.c*: Implementación del algoritmo de Hoshen-Kopelman.

*ns.c*: devuelve en el archivo ns.txt el tamaño de cada uno de los clusters de la red dada como input.

percolacion_d.c: Calcula ns(p) dado cierto p como parámetro. Devuelve ns.txt con los datos para realizar el histograma en python, con 1d/ns.py y devuelve en ns_percolante.txt el tamaño del cluster percolante.

percolacion_kap.c: Calcula $\rho(L)$ según el paper de Kapitulnik. Devuelve los datos en kap.txt. El script kap.py analiza los datos, calcula $D$ la dimensión fractal y genera la figura kap.pdf.

percolacion_m2.c: Calcula directamente en un rango de probabilidades fijo ns y el momento de orden dos m2. Exporta todo en distribucion_ns.txt donde cada fila tiene como primer elemento la probabilidad y después ns para todo s ordenado. Devuelve distribucion_m2.txt el momento de orden dos en el formato PROB M2.

**Como reproducir la guía**

* 1
    * a) ./percolacion_a.o [4,16,32,64,128] 27000
    El código está en percolación.c

    * b) ./percolacion_b.o [4,16,32,64,128] 27000
    Los datos se guardan en percolacion_b_datos.txt
    1b/analisis.py analiza los datos siendo 1b/percolacion_b_L.txt la nomenclatura para los archivos.
    Los gráficos queda en L.pdf en 1b/
    El $P_c$ se puede ver de los datos como el valor más cercano de $F(P)$ a $0.5$

    * c) percolacion_a.o [4,16,32,64,128] 27000
    Además de devolver $P_c$ en la segunda columna da la dispersión

    * d) ./percolacion_d.sh 
    Genera todos los datos necesarios en la carpeta 1d_chi/
    1d_chi/analisis.py genera el análisis de $\chi^2$ a los datos y genera la figura 1d_chi/ns_p.pdf
    Para calcular $\tau$ se usa el script 1d.sh. Esto genera los archivos necesarios en 1d/. El script 1d/ns.py devuelve el valor de tau calculado con el ajuste

* 2
    Con los datos generados en 1.d) se puede calcular la fuerza del cluster percolante con el script 1d_chi/pinfinito.py, pero solo en el rango de probabilidades generado por percolacion_d.sh. Se puede modificar este script para generar en un mayor rango de probabilidades trivialmente.
    
* 3
    percolacion_3.sh genera todos los datos necesarios en 3/
    3/analisis.py genera la figura de $M(L)$ y devuelve en stdout el valor calculado para la dimensión fractal

* Kapitulnik
    percolacion_kap.o 187 27000 pc+0.035
    Este script genera en kap.txt la función $\rho(L)$. El script kap.py calcula la dimensión fractal en stdout y la figura correspondiente en kap.pdf

* 4
    1d_chi/problema4.py calcula f(z) para varios s y plotea todo junto en fz_problema4.pdf

* 5
    1d_chi/problema5.py calcula el valor de sigma usando el metodo propuesto

* 6
    1d_chi/problema6.py calcula m2, todavía no calcula gamma satisfactoriamente. Genera la figura problema6.pdf
