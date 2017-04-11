#!/bin/bash
for prob in `seq 0.50 0.004 0.70`;
do
    time ./percolacion_d.o 32 27000 $prob
    mv ns.txt 1d_chi/ns_$prob.txt
    mv ns_percolante.txt 1d_chi/percolante_$prob.txt
done
