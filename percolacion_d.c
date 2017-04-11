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
    int cluster_percolante;
    // Le puedo dar como parametros el tamaño de la red y la precision 
    // en la probilidad
    prob=0.5;
    if (argc==4) 
     {
       sscanf(argv[1],"%d",&n);
       sscanf(argv[2],"%d",&z);
       sscanf(argv[3],"%f",&prob);
     }

    red=(int *)malloc(n*n*sizeof(int));

      
    int i;
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
      cluster_percolante = percola(red, n);
      ns(red, n, cluster_percolante);
    }
    // Ahora calculo ns(s). En realidad calculo el numero de elementos por
    // clusters, despues en python analizo esos datos


    printf("Probabilidad: %f \n", prob);
    free(red);
    fclose(urandom);

  return 0;
}



