//Se usó primer ajuste
//Rodriguez Colorado Carla Elizabeth
//Méndez Sánchez Erick Jair

import java.util.*;
     public class Memoria{
         public static void main(String args[]){
            Stack <Character> stackLetras = new Stack<Character>();
            char [] memoria;
            memoria = new char[30];
            char [] arrayAux;
            arrayAux = new char[30];
            for(int i=0;i<30;i++)
                memoria[i]='-';
            Scanner sc = new Scanner(System.in);
            int opcion='1', unidadProc, cont=0, cont2=0,j,aux=0;
            int ind=0;
            Character c,caracActual;
            for(c = 'O'; c >= 'A'; --c)
                stackLetras.push(c);
            while(opcion!=-1){
                System.out.println("DIGITA UNA OPCION");
                System.out.println("Asignar(0)/liberar (1)/Salir(-1)");
                opcion= sc.nextInt();
                switch(opcion){
                    case 0:
                        cont=0;
                        for(int i=0;i<30;i++){
                            if(memoria[i]=='-')
                                cont++;
                        }
                        caracActual=stackLetras.peek();
                        System.out.println("Ingresa las unidades que tiene el nuevo proceso"+"("+caracActual+"):");
                        unidadProc=sc.nextInt();
                        for(int i=0;i<30;i++){
                            if(memoria[i]=='-'){
                                j=i;
                                while( j<30 && memoria[j]=='-'){
                                    ++j;
                                    if(unidadProc<=(j-i)){
                                        System.out.println("Entre xd");
                                        for(int k=i ; k<j;k++)
                                            memoria[k]=caracActual;
                                        stackLetras.pop();
                                        j=30;
                                        i=30;
                                        cont=0;
                                    }
                                }
                            }
                        }
                        if(cont >= unidadProc){
                            //copia los procesos compactando a la memoria auxiliar
                            ind=0;
                            aux=0;
                            do{
                            if(memoria[ind]!='-'){
                                arrayAux[aux]=memoria[ind];
                                aux++;
                            }
                            ind++;
                            }while(ind<30);
                            memoria = Arrays.copyOf(arrayAux, 30);
                            //indica que espacio esta liberado
                            if(aux<30){
                            for(ind=aux; ind<30; ind++){
                                    memoria[ind]='-';
                            }
                            }
                            System.out.println("Se compactó la memoria para que el proceso se pudiera ejecutar, la memoria despues de compactacion es:\n");
                            for(int i=0;i<30;i++){
                                System.out.print(memoria[i]);
                            }
                            System.out.println("\n");
                            for(int i=0;i<30;i++){
                            if(memoria[i]=='-'){
                                j=i;
                                while( j<30 && memoria[j]=='-'){
                                    ++j;
                                    if(unidadProc<=(j-i)){
                                        for(int k=i ; k<j;k++)
                                            memoria[k]=caracActual;
                                        stackLetras.pop();
                                        j=30;
                                        i=30;
                                        cont=0;
                                    }
                                }
                            }
                        }
                        }
                    break;
                    case 1:
                        System.out.println("Ingresa el proceso a liberar: ");
                        caracActual = sc.next().charAt(0);
                        for(int i=0;i<30;i++){
                            if(memoria[i]==caracActual){
                                memoria[i]='-';
                                if(stackLetras.peek()!=caracActual)
                                    stackLetras.push(caracActual);
                            }
                        }
                    break;
                }
                System.out.print("\nLa asignacion de memoria ACTUAL es:");
                for(int i=0;i<30;i++){
                        System.out.print(memoria[i]);
                    }
                    System.out.println("\n");
            }
        }

     }