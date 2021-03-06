#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "hoshen.h"
#include "auxiliares.h"

#define Z     27000          // iteraciones
#define N     32            // lado de la red simulada


void  llenar(int *red,int n,float prob);
void numero_s(int *red, int n, float *ns_sinpercolante)
{
    int *lista;
//    int *lista_sp;
    int i,j,k;
    int esta_repetido;
    lista = (int *)malloc(n*n*sizeof(int));
//    lista_sp = (int *)malloc(n*n*sizeof(int));
    int *lista_percolante;
    int contador = 0;
    lista_percolante = (int *)malloc(sizeof(int)*2*n);
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(red[i] == red[n*(n-1)+j]){
                esta_repetido = 0;
                for(k=0;k<contador;k++) if(lista_percolante[k] == red[i]) esta_repetido = 1;
                if(esta_repetido == 0) {
                    lista_percolante[contador] = red[i];
                    contador +=1;
                }
            }
        }
    }
    for(i=0;i<n*n;i++) lista[i] = 0; 
    for(i=0;i<n*n;i++)
    {
        if(red[i]!=0){
            esta_repetido = 0;
            for(j=0;j<contador;j++)if(red[i] == lista_percolante[j]) esta_repetido = 1;
            if(esta_repetido == 0) lista[red[i]] += 1;
        }
    }
    for(i=0;i<n*n;i++) if(lista[i]!=0) ns_sinpercolante[lista[i]] += 1;
    free(lista);
//
//    for(i=0;i<n*n;i++) lista_sp[i] = 0; 
//    for(i=0;i<n*n;i++){ 
//        if(red[i]!=0) {
//            esta_repetido = 0;
//            for(j=0;j<2*n;j++){
//                if(red[i] == lista_percolante[j]) esta_repetido = 1;
//            }   
//            if(esta_repetido == 0) lista_sp[red[i]] += 1;
//        }
//    }
//    for(i=0;i<n*n;i++) if(lista_sp[i]!=0) ns_sinpercolante[lista_sp[i]] += 1;
//    free(lista_sp);
    free(lista_percolante);

}

int main(int argc,char *argv[])
{
    int    *red;
    float  prob;
    FILE *urandom;
    FILE *distribucion_m2;
    distribucion_m2 = fopen("distribucion_m2.txt", "w");
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

      
    int i,j,k;
    // Usar time hace que haga cientos de ciclos con la misma semilla
    urandom = fopen("/dev/urandom", "r");
    // 27000 realizaciones para calcular la probabilidad critica

    float *ns_sinpercolante;
    ns_sinpercolante = (float *)malloc(sizeof(float)*n*n);
    int P = 200;
    float *m2;
    m2 = (float *)malloc(sizeof(float)*P);
    for(j=0;j<P;j++) // Itero sobre el vector de probabilidades
    {
        prob = 0.48+(0.17/P)*j;
    
        for(i=0;i<z;i++)
        {
            fread(&seed, sizeof(seed), 1, urandom);
            srand(seed);
            llenar(red, n, prob);
            hoshen(red, n);
            numero_s(red,n,ns_sinpercolante);
            for(k=0;k<(n*n)/2;k++)
            {
                ns_sinpercolante[k] /= (z*n*n); // Normalizo el ns
                m2[j] += ns_sinpercolante[k]*k*k; // Calculo el m2(p)
            }
        
        }
        //guardo m2
        fprintf(distribucion_m2, "%.4f %.20f\n", prob, m2[j]);
    }
    // Ahora calculo ns(s). En realidad calculo el numero de elementos por
    // clusters, despues en python analizo esos datos

    free(red);
    fclose(distribucion_m2);
    fclose(urandom);

  return 0;
}



