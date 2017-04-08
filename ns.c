#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "hoshen.h"
#include "auxiliares.h"
#include "ns.h"
/* 
 * Esta función calcula el numero de clusters de tamaño s
 */
void ns(int *red, int n) {   
   FILE *archivo;
   archivo=fopen("ns.txt", "a");
   int i, j, k;
   int *lista, *cluster;
   lista=(int *)malloc(n*n*sizeof(int));
   cluster=(int *)malloc(n*n*sizeof(int));

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
   for(i=0;i<k;i++){
      fprintf(archivo, " %i ", cluster[i]);
   }
   free(lista);
   free(cluster);
   fclose(archivo);
}

