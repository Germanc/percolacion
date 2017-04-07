#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "hoshen.h"
#include "auxiliares.h"

#define P     64             // 1/2^P, P=16
#define Z     27000          // iteraciones
#define N     32          // lado de la red simulada


void  llenar(int *red,int n,float prob);
int   percola(int *red,int n);

void imprimir(int *red, int n);

// Este programa calcula F(p)dp dividiendo el intervalo [0,1] en 
// P partes iguales.
int main(int argc,char *argv[])
{
  int    *red;
  float  prob;
  FILE *fp;

  int n=N;
  int z=Z;
// Le puedo dar como parametros el tamaño de la red y la precision 
// en la probilidad, ademas del nombre del archivo donde guardar
// los datos calculados
  if (argc==4) 
     {
       sscanf(argv[1],"%d",&n);
       sscanf(argv[2],"%d",&z);
      fp = fopen(argv[3],"w+");
     }
     else {
     //nombre del archivo por defecto para guardar los datos
       fp = fopen("percolacion_b_datos.txt", "w+");
     }
    
  red=(int *)malloc(n*n*sizeof(int));

  srand(time(NULL));
      
  int i, j;
  float suma = 0.0;
// 27000 realizaciones para calcular la probabilidad critica
    for(j=0;j<P;j++) {
      srand(time(NULL));
      prob=((float) j)/P;
      suma = 0.0;
      for(i=0;i<z;i++)
        {
     
          llenar(red,n,prob);
          hoshen(red,n);
          suma = suma + percola(red,n);
        }
      //El formato es separado por espacios, [p, F(p)]
      fprintf(fp, "%f  %f\n", prob, suma/z);
    }
  free(red);
  fclose(fp);

  return 0;
}


