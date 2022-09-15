//Sistemas Operativos
//Blancas Galicia Braulio Mauricio
//Hernández Alarcón Dulce Azucena
//JAVA

import java.util.*;

public class Main
{
	public static void main(String[] args) {
		
		int num = 0, tamaño,n, sep=0, sep1=0, count = 0;
		char c, r;
		Scanner in = new Scanner(System.in);
		Random random = new Random();
		
		ArrayList<Character> lista = new ArrayList<Character>();
		lista.add('A');
		lista.add('A');
		
		lista.add('B');
		lista.add('B');
		lista.add('B');
		lista.add('B');
		
		lista.add('C');
		lista.add('C');
		lista.add('C');
		lista.add('C');
		
		lista.add('D');
		lista.add('D');
		lista.add('D');
		lista.add('D');
		lista.add('D');
		lista.add('D');
		
		lista.add('E');
		lista.add('E');
		lista.add('E');
		lista.add('E');
		
		lista.add('-');
		lista.add('-');
		lista.add('-');
		
		lista.add('H');
		lista.add('H');
		lista.add('H');
		
		lista.add('I');
		lista.add('I');
		
		lista.add('-');
		lista.add('-');
		
		tamaño = lista.size();
        
        System.out.println("Asignacion actual: \n");
		for (int i = 0; i<tamaño; i++){
	        System.out.print(lista.get(i) + " ");
		 }

		while (num!=2){
		    System.out.println("\nAsignar (0) o liberar (1) Salir (2):");
		    num = in.nextInt();
		
		    switch(num){
		        
		        case 0:
		            r = (char) (random.nextInt(17) + 'I');
		            System.out.println("\n Nuevo proceso (" + r + "):");
		            n = in.nextInt();
		            
		            for (int i = 0; i<tamaño; i++){
		                char s = lista.get(i);
		                if(s=='-'){
		                    sep = i;
		                    count++;
		                }

		            }
		            
		            if(n>count){
		                System.out.println("No es posible realizar la asignación");
		            } else if(n<=count){
		                for (int i = 0; i<tamaño; i++){
		                    char s = lista.get(i);
                            if(s=='-'){
		                        lista.set(i,r);

		                    }
		                    
		                }
		                count=0;
		            } else if(count==0 && n>0){
		                System.out.println("No hay espacios libres");
		            }


		            System.out.println("Asignacion actual: \n");
		            for (int i = 0; i<tamaño; i++){
	                    System.out.print(lista.get(i) + " ");
		            }

		            break;
		        
		        case 1:
		            System.out.println("\nProceso a liberar(ABCDEHI):");
		            c = in.next().charAt(0);
		            for (int i = 0; i<tamaño; i++){
		                char s = lista.get(i);
		                if(s==c){
		                    lista.set(i,'-');
		                }
		            }
		            System.out.println("Asignacion actual: \n");
		            for (int i = 0; i<tamaño; i++){
	                    System.out.print(lista.get(i) + " ");
		            }

		            break;
		        
		        case 2:
		            System.out.println("Hasta luego");
		            break;
		        
		        default:
		        System.out.println("Caso no encontrado");
		        break;
		    }
		}
	}
}
