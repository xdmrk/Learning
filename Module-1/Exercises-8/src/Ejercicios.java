import java.util.Scanner;

public class Ejercicios {
    public static void main(String[] args) {        
        Scanner sc = new Scanner(System.in); //No llamar el Scanner fuera del main
        var salir = false;        

        do {
            System.out.print("""
                    EJERCICIOS DEL MODULO 1 -----------
                    1. Verificar numero
                    9. Venta de camisas

                    0. Salir

                    Elija una opcion:""");
            
            var opcion = sc.nextInt();
            sc.nextLine();

            switch (opcion) {
                case 1: //Ejercicio 1
                    verificarNumero(sc);                    
                    break;

                case 9:
                    ventaCamisas(sc);
                    break;

                case 0:
                    salir = true;
                    break; // si no se pone ejecuta default
            
                default:
                    System.out.println("Opcion incorrecta");
                    break;
            }
            System.out.print("Precione ENTER para continuar ");
            sc.nextLine();

            clear();

        }while(!salir); // hasta que sea true repetir el bloque de codigo
        System.out.println("Hasta luego...");
        sc.close(); 
    }

    private static void ventaCamisas(Scanner sc) {
        clear(); // --> bombillo, extract to method        
        var camisas = 0;
        int precio; 

        // if (camisas <= 0) { // Validacion como filtro
        //     System.out.println("El numero de camisas debe ser positivo: ");
        //     ventaCamisas(sc); // devuelve al inicio de la funcion hasta que el numero sea positivo y pueda pasar al siguiente if
        // }       --> Recursividad, mo recomendado ya que al llamar varias veces el metodo, consume mucha memoria


        do { 
            System.out.print("Cuantas camisas desea comprar: ");
            camisas = sc.nextInt();
            sc.nextLine(); // Limpia buffer, terminar el Scanner, debajo de clear no muestra la siguiente impresion 

            if (camisas > 0) {
                break; //Solo rompera el ciclo si cumple la condicion
            }
        }while (true);


        if (camisas <= 50) {
            precio = 50_000; // _Separador de miles para el codigo, no sale en consola            
        }else if (camisas <= 100) {
            precio = 45_000;            
        }else if (camisas <= 150) {
            precio = 40_000;            
        }else if (camisas <= 200) {
            precio = 35_000;            
        }else{
            precio = 25_000;           
        }// imprime al haberle asignado valor a precio
        System.out.printf(""" 

                    Unidad: $%,d
                    %d camisas cuestan $%,d%n""", precio, camisas, (precio * camisas));
    }

    private static void clear() {
        for (int i = 0; i < 50; i++) {
            System.out.println(); //limpia toda la parte superior del terminal
        }
    }

    private static void verificarNumero(Scanner sc) {
        clear(); // Limipiar consola
        System.out.print("Ingrese el numero real a evaluar: ");
        var real = sc.nextDouble();
        sc.nextLine();

        // Operador ternario
        /*
        var menR = (real == 0) ? "El numero es 0" 
            : (real < 0) 
            ? "El numero es negativo" 
            : "El numero es positivo";

        System.out.println(menR);  */
        // Imprimiendo de una vez
        System.out.println(real == 0 ? "El numero es 0" 
            : real < 0 
            ? "El numero es negativo" 
            : "El numero es positivo");
        

        /* 
        if (real == 0) {
            System.out.println("El numero es 0");
        }else if (real < 0) {
            System.out.println("El numero es negativo");
        }else{
            System.out.println("El numero es positivo");
        }   */      
    }
}
