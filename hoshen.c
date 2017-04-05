#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "hoshen.h"

int hoshen(int *red,int n)
{
  /*
    Esta funcion implementa en algoritmo de Hoshen-Kopelman.
    Recibe el puntero que apunta a la red y asigna etiquetas 
    a cada fragmento de red. 
  */

  int i,j,k,s1,s2,frag;
  int *clase;

  frag=0;
  
  clase=(int *)malloc(n*n*sizeof(int));

  for(k=0;k<n*n;k++) *(clase+k)=frag;
  
  // primer elemento de la red

  s1=0;
  frag=2;
  if (*red) frag=actualizar(red,clase,s1,frag);
  // primera fila de la red

  for(i=1;i<n;i++) 
    {
      if (*(red+i)) 
         {
           s1=*(red+i-1);  
           frag=actualizar(red+i,clase,s1,frag);
         }
    }
  

  // el resto de las filas 

  for(i=n;i<n*n;i=i+n)
    {

      // primer elemento de cada fila

      if (*(red+i)) 
         {
           s1=*(red+i-n); 
           frag=actualizar(red+i,clase,s1,frag);
         }

      for(j=1;j<n;j++) {
          if (*(red+i+j))
          {
            s1=*(red+i+j-1); 
            s2=*(red+i+j-n);

            if (s1*s2>0)
              {
            etiqueta_falsa(red+i+j,clase,s1,s2);
              }
            else 
              { if (s1!=0) frag=actualizar(red+i+j,clase,s1,frag);
                else       frag=actualizar(red+i+j,clase,s2,frag);
              }
          }
      }
    }


  corregir_etiqueta(red,clase,n);

  free(clase);

  return 0;
}

void llenar(int* red, int n, float prob) {
    srand(time(NULL));  
    float valor_aleatorio;
    int i;
    for(i=0; i<(n*n); i++){
        valor_aleatorio = rand()%RAND_MAX;
        if (valor_aleatorio < (prob*RAND_MAX)){
            red[i] = 1;

        }
        else {
            red[i] = 0;
        }
    }

}
int   actualizar(int *red,int *clase,int s,int frag){

    if(s != 0) {
        *red = s;
        frag++;
    } else {
        *red = frag;
        frag++;
    }
    return frag;
}
void  etiqueta_falsa(int *red,int *clase,int s1,int s2){
   if(red[0]) {
       while(clase[s1]<0){
           s1=-clase[s1];
       }
       while(clase[s2]<0){
           s2=-clase[s2];
       }
       if(s1<s2) {
           clase[s2] = -s1;
           clase[s1] = s1;
           red[0] = s1;
       } else {
            clase[s1] = -s2;
            clase[s2] = s2;
            red[0] = s2;
       }
   }
}
void  corregir_etiqueta(int *red,int *clase,int n){
    int i;
    int s;
    for(i=0;i<(n*n);i++) {
        s = red[i];
        while(clase[s]<0) {
            s = -clase[s];
            red[i] = s;
        }
    }
}
int   percola(int *red,int n){
    int i;
    int j;
    int se_repite = 0;
    for(i=0; i<n; i++) {
        for(j=0; j<n; j++) {
            if(red[i] == red[(n-1)*n+j]) {
                if(red[i]) {
                se_repite = 1;
                }
            }
        }
}
    return se_repite;
}
