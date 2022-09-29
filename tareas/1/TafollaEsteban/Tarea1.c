#include<stdio.h>
#include <stdlib.h>
#include<time.h>

typedef struct{
	int inicio;
	int fin; 
	char nomProceso;
	int fila;
}proceso;

typedef struct{
	int inicio;
	int fin;
	char nomParticion;
	
}particiones;

typedef struct{
	char info[30];
	int noParticiones;
	int noProc;
}memoria;

void imprimeMemoria(memoria m1){
	printf("Estado de la memoria: ");
	for(int i = 0; i<30; ++i){
		printf("%c",m1.info[i]);
	}
	printf("\n");
}

memoria compacta(memoria m1){
	int aux;
	int aux2=0;
	int i=0;
	while(i<30){
		if(m1.info[i] == '-' &&i+aux2<30){
			aux=i;
			while(aux<30){
				m1.info[aux] = m1.info[aux+1];
				if(aux==29) {
					m1.info[aux] = '-';
					aux2++;
				}
				aux++;
			}
			
		}
		else i++; 
	}
	
	return m1;
}
memoria creaProceso(int tamano, char nombre, memoria m1, particiones memoriaP[], proceso memoriaPros[]){
	if(tamano <= 15 && tamano >=2){
		for(int i = 0; i < m1.noParticiones; ++i){
			if((memoriaP[i].fin - memoriaP[i].inicio + 1) >= tamano &&  m1.info[memoriaP[i].inicio]=='-'){
				if(m1.noParticiones-1==i){
					memoriaP[i+1].fin = memoriaP[i].fin;
					
					memoriaP[i].fin = memoriaP[i].inicio+tamano-1;
					
					//Evita que existan particiones con tamaño 0
					if(memoriaP[i+1].fin != memoriaP[i].fin ) {
						memoriaP[i+1].inicio = memoriaP[i].fin + 1;
						m1.noParticiones++;
						
					}
					else {
						// m1.noParticiones--;
						// for(int cont = i; cont < m1.noParticiones;cont++){
							// memoriaP[cont]=memoriaP[cont];
						}
					}
				// printf("valor de i %d\n", i);
				printf("Datos de particiones. Inicio: %d, fin: %d\n",memoriaP[i].inicio,memoriaP[i].fin);	
				printf("Datos de particiones. Inicio: %d, fin: %d\n",memoriaP[i+1].inicio,memoriaP[i+1].fin);	
				// printf("%d\n", memoriaP[i].inicio );
				// printf("%d\n", memoriaP[i].fin );
				
				
				// 2.-Almacenamos la informacion de nuestro proceso 
				memoriaPros[m1.noProc].inicio = memoriaP[i].inicio;
				// printf("%d\n", memoriaPros[m1.noProc].inicio );
	
				memoriaPros[m1.noProc].fin = memoriaP[i].fin;
				// printf("%d\n", memoriaPros[m1.noProc].fin );
				
				memoriaPros[m1.noProc].nomProceso = nombre;
				// printf("%c\n", memoriaPros[m1.noProc].nomProceso );
		
				memoriaPros[m1.noProc].fila = 0;
				// printf("%d\n", memoriaPros[m1.noProc].fila );
				
				// 3.-Modificamos la memoria 
				for(int i = memoriaPros[m1.noProc].inicio; i <= memoriaPros[m1.noProc].inicio+tamano-1; i++){
					m1.info[i] = memoriaPros[m1.noProc].nomProceso;
				}
				m1.noProc++;
				
				// printf("%s\n",m1.info);
				break;
				
				
			}
			// else{
				// printf("No hay espacio en memoria \n");
			// }
		}
	}
	else printf("El proceso es muy grande o muy pequeno\n");
	return m1;
}


memoria terminaProceso(char nombre, memoria m1, particiones memoriaP[], proceso memoriaPros[]){
	int i = 0;
	//Busaca el proceso por su nombre
	while(nombre != memoriaPros[i].nomProceso && i < m1.noProc){
		i++;
	}
	
	if(i == m1.noProc) printf("El proceso no esta en memoria\n");
	else{
		//lo encuentra y borra la informacion en memoria
		int auxInicio = memoriaPros[i].inicio; 
		
		int auxFin = memoriaPros[i].fin;
		// printf("%d\n",auxInicio);
		// printf("%d\n",auxFin);
		for(int j = auxInicio; j <= auxFin; j++){
			m1.info[j]='-';
		}
		//Recorre el arreglo de procedimiento y le resta uno
		for(int j = i; j < m1.noProc; j++){
			memoriaPros[j]=memoriaPros[j+1];
		}
		m1.noProc--;
	} 	
	return m1;
}

memoria acomaPosicion(memoria m1, particiones memoriaP[], proceso memoriaPros[]){
	char nombre = m1.info[0];
	int inicio = 0;
	int final;
	int aux = 0;
	int j;
	for(int i=0; i<30; i++){
		if(m1.info[i]!='-'){
			if(nombre != m1.info[i]){
				final = i-1;
				memoriaP[aux].inicio = inicio;
				memoriaP[aux].fin = final;
				inicio = final+1;
				j=0;
				while(memoriaPros[j].nomProceso!= nombre){
					j++;
				}
				memoriaPros[j].inicio = memoriaP[aux].inicio;
				memoriaPros[j].fin = final;
				nombre = m1.info[i];
				aux++;
			}
		}
		else{
			if(nombre != '-'){
				memoriaP[aux].inicio = inicio;
				memoriaP[aux].fin = i-1;
				j=0;
				while(memoriaPros[j].nomProceso!= nombre){
						j++;
				}
				memoriaPros[j].inicio = memoriaP[aux].inicio;
				memoriaPros[j].fin =i-1;
				inicio = i;
				nombre = '-';
				aux++;
			}
			else{
				memoriaP[aux].inicio = inicio;
				memoriaP[aux].fin = 29;
			}
		}
	}
	m1.noParticiones = aux+1;
	return m1;
}


int main(){
	
	particiones memoriaP[15]; //numero maximo de particiones posibles
	proceso memoriaPros[15]; //numero maximo de procesos posibles
	memoria m1;
	char menu;
	char nombre;
	int tam;
	//inicializando memoria
	for(int i=0; i<30; i++){
		m1.info[i] = '-';
	}
	
	m1.noParticiones = 1;
	m1.noProc = 0;
	//inicio y fin de la particion inicial
	memoriaP[0].inicio = 0;
	memoriaP[0].fin = 29;
	do{
		printf("Simulador de asignacion de memoria contigua por el primer ajuste\n");
		printf("Ingrese 1 para crear proceso 0 para eliminar y 2 para salir: \n");
		scanf(" %c",&menu);
		if(menu == '1'){
			printf("Ingresa una simbolo diferente de '-': ");
			scanf(" %c", &nombre);
			
			if(nombre!='-'){
				printf("Ingresa un tamano entre 2 y 15: ");
				scanf(" %i", &tam);
			
				m1 = creaProceso(tam, nombre, m1, memoriaP, memoriaPros);
				imprimeMemoria(m1);
			}
			
		}
		if(menu == '0'){
			for(int i=0; i<m1.noProc; i++){
				if(memoriaPros[i].nomProceso == nombre){
					m1 = terminaProceso(nombre,m1, memoriaP, memoriaPros);
					imprimeMemoria(m1);
				}
			}
			
		}
	}while(menu != '2');
	return 0;
}



