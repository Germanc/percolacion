#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "hoshen.h"
#include "auxiliares.h"

#define Z     1000          // iteraciones
#define N     187          // lado de la red simulada


void  llenar(int *red,int n,float prob);
int red_mayor(int *red, int n);

int main(int argc,char *argv[])
{
    int    *red;
    float  prob;
    FILE *urandom;
    FILE *datos;
    int seed;
    float *rho, *L;

    datos = fopen("kap.txt", "w");
    int n=N;
    int z=Z;
    // Le puedo dar como parametros el tamaño de la red y la precision 
    // en la probilidad
    prob=0.6277;
    if (argc==4) 
     {
       sscanf(argv[1],"%d",&n);
       sscanf(argv[2],"%d",&z);
       sscanf(argv[3],"%f",&prob);
     }

    rho = (float *)malloc(sizeof(float)*n);
    L = (float *)malloc(sizeof(float)*n);

    red=(int *)malloc(n*n*sizeof(int));

      
    int i,j,k,h;
    float pd;
    int cantidad = 0;
    for(j=3;j<n;j=j+2){
        rho[j] = 0;
        L[j] = j;
    }
    // Usar time hace que haga cientos de ciclos con la misma semilla
    urandom = fopen("/dev/urandom", "r");
    int *subred;
    subred = (int *)malloc(sizeof(int)*n*n);
    fread(&seed, sizeof(seed), 1, urandom);
    srand(seed);

    for(i=0;i<z;i++)
    {

      llenar(red, n, prob);
      hoshen(red, n);
      pd=0;

      // Calculo la probabilidad de ocupacion
      for(j=0;j<n*n;j++){
         if(red[j]!=0) pd=pd+1;
      }

      int numero_maximo = red_mayor(red, n);
//      imprimir(red, n);
//      printf("Numero maximo: %i\n", numero_maximo);
        // Verifico que la probabilidad de ocupación sea cercana a a pedida y
      // que el elemento central de la red pertenezca al cluster mas grande

      if(fabs(prob-pd/(n*n))<0.005 && red[((n*n-1)/2)+1] == numero_maximo) {
          cantidad = cantidad + 1;
          printf("Cantidad %i\n", cantidad);
          for(j=3;j<n;j=j+2){

              // Armo la subred de tamaño j*j alrededor del elemento central de la
              // red
              for(k=0;k<j;k++){
                  for(h=0;h<j;h++){
                      subred[k*j+h] = red[((n-j)/2+1+k)*n+(n-j)/2+1+h-n];
                  }
              }

                      /*
                 *
                 * Tengo que buscar el cluster mas grande
                 * Después verificar si el nodo central pertenece a ese cluster
                 * Después contar el número de nodos en un cuadrado de lado L
                 * que pertenece a ese cluster, eso es M(L).
                 * Todo esto hay que promediarlo
                 */

                  for(k=0;k<(j*j);k++){
                      if(subred[k] == numero_maximo) rho[j] = rho[j]+1;
                  }

          }
      }
    }
    for(i=3;i<n;i=i+2)
    {
      fprintf(datos, "%f %f\n", rho[i]/(i*i*cantidad), L[i]);
    }

    free(red);
    fclose(urandom);
    free(L);
    free(rho);
    free(subred);

  return 0;
}


int red_mayor(int *red, int n){
    int i,j;
    int k = 0;
    int *lista, *cluster;
    lista = (int *)malloc(sizeof(int)*n*n);
    cluster = (int *)malloc(sizeof(int)*n*n);

   for(i=0;i<(n*n);i++){
       int se_repite = 0;
       if(red[i] != 0){
            for(j=0;j<k;j++){
                if(red[i] == lista[j]){
                    se_repite = 1;
                    cluster[j] = cluster[j]+1;
                    break;
                }
            }
            if(se_repite == 0){
                lista[k] = red[i];
                cluster[k] = 1;
                k = k + 1;
            }
       }
   }

    int ultimo_tamanio = 0;
    int ultima_lista = 0;
    for(i=0;i<k;i++){
//        printf("cluster i; %i - lista i: %i\n", cluster[i], lista[i]);
        if(cluster[i]>ultimo_tamanio) {
            ultimo_tamanio = cluster[i];
            ultima_lista = lista[i];
        }
    }

    free(lista);
    free(cluster);
    return ultima_lista;
}
