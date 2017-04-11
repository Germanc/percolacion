#!/bin/bash

for i in 4 16 32 64 18
do
    time ./percolacion_a.o $i 27000
    mv ns.txt 3/ns_$i.txt
    mv ns_percolante.txt 3/percolante_$i.txt
done
