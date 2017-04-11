#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "hoshen.h"

// Imprime en pantalla una red *red de n*n
void imprimir(int *red, int n){
    int i;
    for(i=0;i<(n*n);i++) {
        if((i%n)==0) {
            printf("\n");
        }
        else {
            printf(" %i ", red[i]);
        }
    }
    printf("\n \n");

}

// Calcula si existe un nodo que conecte la parte superior
// e inferior de la red. Devuelve 0 (falso) o 1 (verdadero)
int   percola(int *red,int n) {
    int i,j,se_repite;
    se_repite = 0;
    int cluster_percolante = 0;
    for(i=0;i<n;i++) {
        for(j=0;j<n;j++) {
           if(red[i] == red[(n-1)*n+j]){
               if(red[i] != 0) { 
                   se_repite = 1;
                   cluster_percolante = red[i];
               }
           }
        }
    }
    if(se_repite){
        se_repite = cluster_percolante;
    }
    return se_repite;
}

