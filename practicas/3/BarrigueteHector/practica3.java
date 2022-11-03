import java.util.Scanner;
import java.util.ArrayList;

public class practica3 {
    public static void main(String[] args) {
        Scanner nao = new Scanner(System.in);
        
        ArrayList<String> lista = new ArrayList<String>();

        System.out.print("Ingresa el nuevo proceso: ");
        String proceso = nao.nextLine();
        
        System.out.print("Ingresa su longitud: ");
        int longitud = nao.nextInt();
        
        for (int i = 0; i < longitud; i++) {
            lista.add(proceso);
        }
        
        System.out.println("Lista de procesos: " + lista);

        nao.close();
    }
}