#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "hoshen.h"
#include "auxiliares.h"
#include "ns.h"

#define P     16             // 1/2^P, P=16
#define Z     27000          // iteraciones
#define N     30            // lado de la red simulada


void  llenar(int *red,int n,float prob);

int main(int argc,char *argv[])
{
    int    *red;
    float  prob;
    FILE *urandom;
    int seed;

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
      
    int i, j;
    float denominador;
    float suma = 0.0;
    float sigma = 0.0;
    float suma_cuadrado = 0.0;
    // Usar time hace que haga cientos de ciclos con la misma semilla
    urandom = fopen("/dev/urandom", "r");
// 27000 realizaciones para calcular la probabilidad critica
    for(i=0;i<z;i++)
    {
      prob=0.5;
      denominador=2.0;

      fread(&seed, sizeof(seed), 1, urandom);
      srand(seed);
    // Dentro de este bucle busco pc
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
      // Sumo para calcular despues el valor medio y el sigma
        ns(red, n);
      suma = suma + prob/z;
      suma_cuadrado = suma_cuadrado + prob*prob/z;
    }
    // Ahora calculo ns(s). En realidad calculo el numero de elementos por
    // clusters, despues en python analizo esos datos


    sigma = sqrt(suma_cuadrado - suma*suma);
    printf("%f %f", suma, sigma);
    free(red);
    fclose(urandom);

  return 0;
}



