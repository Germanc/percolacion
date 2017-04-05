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
// Le puedo dar como parametros el tamaño de la red y la precision 
// en la probilidad
  if (argc==3) 
     {
       sscanf(argv[1],"%d",&n);
       sscanf(argv[2],"%d",&z);
     }
    
  red=(int *)malloc(n*n*sizeof(int));

  prob=0.5;
  srand(time(NULL));
      
  int i, j;
  float denominador;
  float suma = 0.0;
// 27000 realizaciones para calcular la probabilidad critica
  for(i=0;i<z;i++)
    {
      prob=0.5;
      denominador=2.0;
 
      srand(time(NULL));

      for(j=0;j<P;j++)
        {
          llenar(red,n,prob);
      
          hoshen(red,n);
        
          denominador=2.0*denominador;

          if (percola(red,n)) {
             prob+=(-1.0/denominador);
          } else  {
              prob+=(1.0/denominador);
          }
        }
      suma = suma + prob;
    }

  printf("%f", suma/Z);
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

int   percola(int *red,int n) {
    int i,j,se_repite;
    se_repite = 0;
    for(i=0;i<n;i++) {
        for(j=0;j<n;j++) {
           if(red[i] == red[(n-1)*n+j]){
               if(red[i] != 0) se_repite = 1;
           }
        }
    }
    return se_repite;
}
