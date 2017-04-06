all: percolacion_a percolacion_b
percolacion_a: percolacion.c hoshen.c
	gcc -o percolacion_a.o percolacion.c hoshen.c -I -O3 -Wall -g
percolacion_b: percolacion_b.c hoshen.c
	gcc -o percolacion_b.o percolacion_b.c hoshen.c -I -O3 -Wall -g
clean:
	rm percolacion_a.o percolacion_b.o