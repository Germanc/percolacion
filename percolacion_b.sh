#!/bin/bash
./percolacion_b.o 4 27000 percolacion_b_4.txt
./percolacion_b.o 16 27000 percolacion_b_16.txt
./percolacion_b.o 32 27000 percolacion_b_32.txt
./percolacion_b.o 64 27000 percolacion_b_64.txt
./percolacion_b.o 128 27000 percolacion_b_128.txt

mv percolacion_b_*.txt 1b/
