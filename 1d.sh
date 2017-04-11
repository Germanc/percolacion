#!/bin/bash
./percolacion_a.o 4 27000
mv ns.txt ns_4.txt
./percolacion_a.o 16 27000
mv ns.txt ns_16.txt
./percolacion_a.o 32 27000
mv ns.txt ns_32.txt
./percolacion_a.o 64 27000
mv ns.txt ns_64.txt
./percolacion_a.o 128 27000
mv ns.txt ns_128.txt

mv ns_*.txt 1d/
