#!/bin/bash
for prob in `seq 0.5 0.004 0.7`;
do
    ./percolacion_d.o 128 27000 $prob
    mv ns.txt 1d_chi/ns_$prob.txt
done
