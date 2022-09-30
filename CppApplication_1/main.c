#include <stdio.h>
#include <stdlib.h>

/* Zuniga Salgado Luis
 * Tarea 1: asignador de memoria
 * utilizando primer ajuste
 */
int main() {
    //cont= continuar, proc= nombre del proceso
    char cont,proc;
    cont=' ';
    proc=' ';
    //c= choice, pCont= contador proc, sizeP= tam proc, i,j=contadores FOR
    //mAs= guarda posicion memoria, f= bandera
    int c,pCont,sizeP,i,mAs,f,j;
    //mCont= tamaño del espacio en memoria libre por bloque
    int mCont;
    pCont=0;
    char mem[30]; //mem= la memoria total que tenemos
    //llenamos memoria con espacios vacios
    for(i=0; i<30;i++){
        mem[i]='-';        
    }
    //e imprimimos por primera vez
    printf("\n");
    for(i=0; i<30;i++){
        printf("%c",mem[i]);
    }
    //iniciamos el menu
    do{ 
        printf("\nAsignar memoria[0] o liberar proceso[1]?");
        scanf("%d",&c);
        //Si intentamos borrar procesos y no tenemos ninguno aun lo indica
        if(c==1 && pCont==0){
            printf("\nNo hay proceso que liberar");
        }else{
            //Caso asignar nuevo proceso a memoria
            if(c==0){
                //pedimos datos
                printf("\nNombre del proceso?[Un solo caracter]:");
                fpurge(stdin);
                scanf("%c",&proc);
                printf("\nTamanio del proceso?:");
                scanf("%d",&sizeP);
                //reseteamos variables a usar
                mCont=0;
                f=0;
                j=0;
                //buscamos por un espacio vacio en memoria
                for(i=0;i<30;i++){
                    //Si es el primer espacio que encontramos
                    if(mem[i]=='-'&& f==0){
                        //mAs guarda la ubicacion
                        mAs=i;
                        //incrementamos contador de espacio vacio
                        mCont++;
                        //indicamos que ya encontramos un espacio disponible
                        f=1;
                    }else{
                        //Si no es el primero, solo aumentamos mCont
                        if(mem[i]=='-')
                            mCont++;
                    }
                    //verificamos que nuestro proceso quepa en el espacio
                    if(mCont>=sizeP){
                        //si lo hace, vamos a la posicion inicial, 
                        for(j=mAs;j<(sizeP+mAs)&& j<30;j++)
                            //y empezamos a llenar
                            mem[j]=proc;
                        f=2;// indicamos que lo hemos llenado
                        pCont++;//aumentamos el contador de procesos
                        break;//terminamos el ciclo de asignacion
                    }
                    //Si el espacio no fue suficiente AKA no se asigno y 
                    //encontramos otro proceso
                    if(mem[i]!='-' && f!=2){
                        mAs=-1;//quitamos el marcador de memoria
                        mCont=0;//reiniciamos contador de espacio
                        f=0;//y reseteamos bandera
                    }   
                }
                if(f!=2) //Si al terminar no se pudo asignar el proceso
                    printf("\nNo se pudo asignar el proceso");
            }
            //caso liberar memoria
            if(c==1){//pedimos el proceso a eliminar
                printf("\nIndique el proceso a liberar: ");
                fpurge(stdin);
                scanf("%c",&proc);
                for(i=0;i<30;i++){//cada coincidencia del nombre en memoria
                    if(mem[i]==proc){
                        mem[i]='-';//es borrada
                        f=3;//indicamos que se pudo borrar
                    }
                }
                if(f==3){//imprimimos exito
                    printf("\nProceso borrado con exito");
                    pCont--;
                }
                else//o si no se pudo borrar por alguna razon
                    printf("\nNo se encontro el proceso");
            }
        }
        printf("\n");
        for(i=0; i<30;i++){//reimprimimos memoria para que se vea contenido
            printf("%c",mem[i]);
        }
        printf("\nDesea continuar?[y/N]");
        fpurge(stdin);
        scanf("%c",&cont);
    }while(cont!='n' && cont!='N');
    return (EXIT_SUCCESS);
}

