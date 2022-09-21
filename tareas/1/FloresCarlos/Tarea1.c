//Tarea 1. Asignación en memoria contigua
//Alumno: Flores Valencia Carlos Enoc

//Se utiliza la estrategia de primer ajuste

#include <stdio.h>
#include <stdlib.h>

void imp_mem(char A[30]); //Funcion para imprimir memoria
void asig_mem(char A[30]); //Funcion para asignar memoria a proceso
void lib_mem(char A[30]); //Funcion para liberar proceso

char memoria[30]; //Cadena que simula la memoria
int i; //Auxiliar para recorrer memoria

main(){
	int salida = 0; //Bandera para salir del menu
	int op; //Solicitud
	for(i=0;i<30;i++){ //Se crea la configuracion inicial de la memoria
		memoria[i]='-';
	}
	while(salida == 0){
		imp_mem(memoria);
		printf("\nAsignar proceso(0),  Liberar proceso(1),  Salir(2)\n");
		scanf("%d", &op);
		switch(op){
			case 0:
				asig_mem(memoria);
				break;
			case 1: 
				lib_mem(memoria);
				break;
			case 2: 
				printf("\nFin de asignacion\n");
				salida = 1;
				break;
			default:
				printf("\nOpcion no valida");
				break;
		}
	}
	return 0;
}

void imp_mem(char A[30]){ //Funcion para imprimir memoria
	printf("\nAsignacion actual de la memoria\n");
	for(i=0;i<30;i++){
		printf("%c", memoria[i]);
	}
}

void asig_mem(char A[30]){ //Funcion para asignar memoria a proceso
	int atam, tam; //Tamaño de proceso
	char P; //Nombre del proceso
	int caux; // Contador auxiliar para contar espacios disponibles
	int j; //Auxiliar para asignar proceso
	int cmaux; //Auxiliar para ayudar en el proceso de compactacion
	char Paux; //Auxiliar para ayudar en el proceso de compactacion
	printf("\nIngrese el nombre del proceso(A-Z): ");
	scanf(" %c", &P);
	printf("\nIngrese el tamano del proceso (2-15): ");
	scanf("%d", &atam);
	if (atam >=2 && atam <=15 ){
		tam = atam;
	}else{
		printf("Tamano incorrecto\n");
		return;	
	}
	caux=0;
	for(i=0;i<30;i++){ //Recorre memoria por primera vez
		if(memoria[i]=='-'){
			caux++;
		}else{
			caux = 0;
		}
		if(caux == tam){
			for(j=0;j<tam;j++){
				memoria[i-j]=P;
			}
			return;
		}
	}
	printf("\n**Compactacion requerida**\n"); //En caso de no poder asignar memoria
	int r; //Auxiliar para repetir la compactacion hasta poder asignar memoria
	for(r=0;r<3;r++){ // Repite el recorrido de la memoria para evitar espacios entre procesos
		i=0;
		while(i<30){ // Optimiza los espacios vacíos
			if(memoria[i]=='-'){
				cmaux=i;
				while(cmaux<30){
					Paux = memoria[cmaux];
					memoria[cmaux] = memoria[cmaux+1];
					memoria[cmaux+1] = Paux;
					cmaux++;
				}
				memoria[29]='-';	
			}
			i++;
		}
	}
	imp_mem(memoria);
	caux=0;
	for(i=0;i<30;i++){ //Recorre memoria tras compactacion
		if(memoria[i]=='-'){
			caux++;
		}else{
			caux = 0;
		}
		if(caux == tam){
			for(j=0;j<tam;j++){
				memoria[i-j]=P;
			}
			return;
		}
	}
	printf("\n**Espacio insuficiente en memoria, libere algun proceso**\n");
}

void lib_mem(char A[30]){
	char P; //Nombre del proceso
	int eP=0; //Bandera para detectar proceso
	printf("\nIngrese el nombre del proceso(A-Z): ");
	scanf(" %c", &P);
	for(i=0;i<30;i++){ //Busca proceso
		if(memoria[i]==P){
			eP=1;
		}
	}
	switch(eP){
		case 0:
			printf("\n**Proceso %c no encontrado, por favor verifique la existencia del proceso**\n", P);
			break;
		case 1:
			for(i=0;i<30;i++){ //Recorre memoria para liberar proceso
				if(memoria[i]==P){
					memoria[i]='-';
				}
			}
			break;
	}
}
