#include <stdio.h>
#include <stdlib.h>

int main()
{
    int edades[10],nEdades=0,k,vp; //vp = valor prueba
    for (k=0;k<10;k++)
        edades[k]=0;
    printf("\nInsertar Edades\n");
    for (k=0;k<10;k++){
        printf("Edad %d: ",(k+1));
        scanf("%d",&vp);
        if(vp<=0)
            k=10;
        else{
            edades[k]=vp;
            nEdades++;}
        }
    printf("\nNo. de Edades Almacenadas: %d",nEdades);
    printf("\nArreglo Completo:\n");
    for (k=0;k<10;k++)
        printf("[%d] = %d\n",k,edades[k]);
    vp=0;
    for (k=0;k<nEdades;k++){
        if(edades[k]<18)
            vp++;}
    printf("\nNo. de Edades Almacenadas: %d",nEdades);
    printf("\nArreglo Con Edades:\n");
    for (k=0;k<nEdades;k++)
        printf("[%d] = %d\n",k,edades[k]);
    printf("No. de Menores de Edad: %d\n",vp);

    return 0;}
