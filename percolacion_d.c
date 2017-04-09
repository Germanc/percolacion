#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "hoshen.h"
#include "auxiliares.h"
#include "ns.h"

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
    prob = 0.5;
    // Le puedo dar como parametros el tamaño de la red y la precision 
    // en la probilidad
    if (argc==3) 
     {
       sscanf(argv[1],"%d",&n);
       sscanf(argv[2],"%d",&z);
       sscanf(argv[3],"%f",&prob);
     }

    red=(int *)malloc(n*n*sizeof(int));

    prob=0.5;
      
    int i;
    float suma = 0.0;
    float sigma = 0.0;
    float suma_cuadrado = 0.0;
    // Usar time hace que haga cientos de ciclos con la misma semilla
    urandom = fopen("/dev/urandom", "r");
    // 27000 realizaciones para calcular la probabilidad critica
    for(i=0;i<z;i++)
    {
      fread(&seed, sizeof(seed), 1, urandom);
      srand(seed);
      llenar(red, n, prob);
      hoshen(red, n);
    // Dentro de este bucle busco pc
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



