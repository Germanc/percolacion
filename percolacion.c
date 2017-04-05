#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "hoshen.h"

#define P     16             // 1/2^P, P=16
#define Z     27000          // iteraciones
#define N     30            // lado de la red simulada


void  llenar(int *red,int n,float prob);
int   percola(int *red,int n);

void imprimir(int *red, int n);

int main(int argc,char *argv[])
{
  int    *red;
  float  prob;

  int n=N;
  int z=Z;

  if (argc==3) 
     {
       sscanf(argv[1],"%d",&n);
       sscanf(argv[2],"%d",&z);
     }
    
  red=(int *)malloc(n*n*sizeof(int));

  prob=0.5;
  srand(time(NULL));
  llenar(red,n,prob);
      
  imprimir(red,n);
  hoshen(red,n);
  imprimir(red,n);
  free(red);

  return 0;
}


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
