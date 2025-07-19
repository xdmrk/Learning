import java.util.Scanner;

public class _3_While {
    public static void main(String[] args) {

        int intentos = 0;
        while (intentos < 3) { // Se ejecuta hasta que intentos sea 3
            System.out.println("Clave incorrecta"); // Se ejecuta hasta que la (condicion) sea false
            intentos ++;            
        }


        boolean activo = true;
        while (activo) {
            System.out.println("Procesando...");
            break; // --> sin el break seria un ciclo infinito            
        }


        int numero;
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero positivo: ");
        numero = sc.nextInt();

        while (numero < 0) { // Normalmente es un validador de errores
            System.out.println("no es un numero positivo"); // Se ejecuta hasta que la (condicion) sea false
            numero = sc.nextInt();           
        }


        sc.close();
    }
}
