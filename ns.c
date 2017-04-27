#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "hoshen.h"
#include "auxiliares.h"
#include "ns.h"
/* 
 * Esta función calcula el numero de clusters de tamaño s
 */
void ns(int *red, int n, int cluster_percolante) {   
   FILE *archivo;
   FILE *percolante;
   archivo=fopen("ns.txt", "ab");
   percolante = fopen("ns_percolante.txt", "a");
   int i, j, k;
   int *lista, *cluster;
   lista=(int *)malloc(n*n*sizeof(int));
   cluster=(int *)malloc(n*n*sizeof(int));

   for(i=0;i<(n*n);i++) lista[i] = 0;
   for(i=0;i<(n*n);i++) cluster[i] = 0;
   // Cuento el tamaño de lista y cluster
   k = 0;
   /*
    * Recorro toda la red. Si el numero que tiene asignado el cluster
    * ya fue usado, aumento en uno el contador de numero de nodos 
    * para ese cluster. Si nunca aparecio, lo agrego en lista y le asigno
    * un 1 al numero de nodos para ese nuevo cluster
    */
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
   /*
    * Ahora tengo:
    * lista[k] = lista de todos los clusters distintos de la red
    * cluster[k] = numero de nodos que tiene cada uno de los clusters de la red
    */
   int *lista_percolante;
   int contador = 0;
   int esta_repetido;
   lista_percolante = (int *)malloc(sizeof(int)*2*n);
   for(i=0;i<n;i++){
       for(j=0;j<n;j++){
           if(red[i] == red[n*(n-1)+j]){
               esta_repetido = 0;
               for(k=0;k<contador;k++) if(lista_percolante[k] == red[i]) esta_repetido = 1;
                   if(esta_repetido == 0) {
                       lista_percolante[contador] = red[i];
                       contador += 1;

                   }   
           }
       }
   }
   for(i=0;i<k;i++){
      fprintf(archivo, " %i ", cluster[i]);
      for(j=0;j<contador;j++){
          if(lista[i] == lista_percolante[j]){
              fprintf(percolante, "%i\n", cluster[i]);
          }
      }

   }
   free(lista_percolante);
   free(lista);
   free(cluster);
   fclose(archivo);
   fclose(percolante);
}

