#!/bin/bash
for i in 4 16 32 64 128
do
    for prob in `seq 0.50 0.004 0.70`;
    do
        date
        ./percolacion_d.o $i 27000 $prob
        mv ns.txt 1d_chi/$i/ns_$prob.txt
        mv ns_percolante.txt 1d_chi/$i/percolante_$prob.txt
    done
done
