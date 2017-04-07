all: percolacion_a percolacion_b
percolacion_a: percolacion.c hoshen.c auxiliares.c
	gcc -o percolacion_a.o percolacion.c hoshen.c auxiliares.c -I -O3 -Wall -g -lm
percolacion_b: percolacion_b.c hoshen.c auxiliares.c
	gcc -o percolacion_b.o percolacion_b.c hoshen.c auxiliares.c -I -O3 -Wall -g -lm
clean:
	rm percolacion_a.o percolacion_b.o
