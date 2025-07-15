import java.util.Scanner;

public class _5_CalculadoraModular {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        mostrarMenu(sc); // Bombillo -> create meth

        sc.close();
    }

    private static void mostrarMenu(Scanner x) {
        int opcion = -1; // Inicializamos con un valor que no sea 0 para entrar al do-while
        do {
            System.out.println("Bienvenidos a la CALCULADORA MODULAR");
            System.out.println("=========================================");
            System.out.println("""
                    1. Suma
                    2. Resta
                    3. Multiplicacion
                    4. Modulo
                    5. Division
                    0. Salir
                    """);
            opcion = leerEntero(x, "Ingrese su opcion: ");

            switch (opcion) {
                case 1:
                    suma(x);
                    break;

                case 2:
                    resta(x);
                    break;

                case 3:
                    multiplicacion(x);
                    break;

                case 4:
                    modulo(x);
                    break;

                case 5:
                    division(x);
                    break;

                case 0:
                    System.out.println("Saliendo.....");
                    break;

                default:
                    System.out.println("Opcion invalida");
                    break;
            }
        } while (opcion != 0);
        System.out.println("Hasta pronto...");
    }

    private static int leerEntero(Scanner input, String mensaje) {
        System.out.print(mensaje);
        var entrada = input.nextInt();
        input.nextLine();

        return entrada;

    }

    private static void suma(Scanner yuca) { // va a pedir dato, tarigo el scanner
        System.out.println("\n    SUMA");
        var num1 = leerEntero(yuca, "Ingrese el primer operador: ");
        var num2 = leerEntero(yuca, "Ingrese el segundo operador: ");

        System.out.println("La suma es: " + (num1 + num2));

        System.out.println("Precione ENTER para continuar");
        yuca.nextLine();

    }

    private static void resta(Scanner pandeBono) {
        System.out.println("\n    RESTA");
        var num1 = leerEntero(pandeBono, "Ingrese el primer operador: ");
        var num2 = leerEntero(pandeBono, "Ingrese el segundo operador: ");

        System.out.println("La resta es: " + (num1 - num2));

        System.out.println("Precione ENTER para continuar");
        pandeBono.nextLine();
    }

    private static void multiplicacion(Scanner buñuelo) {
        System.out.println("\n    MULTIPLICACION");
        var num1 = leerEntero(buñuelo, "Ingrese el primer operador: ");
        var num2 = leerEntero(buñuelo, "Ingrese el segundo operador: ");

        System.out.println("La multiplicación es: " + (num1 * num2));

        System.out.println("Precione ENTER para continuar");
        buñuelo.nextLine();
    }

    private static void division(Scanner empanada) {
        System.out.println("\n    DIVISION");
        var num1 = leerEntero(empanada, "Ingrese el primer operador: ");
        var num2 = leerEntero(empanada, "Ingrese el segundo operador: ");

        if (num2 == 0) {
            System.out.println("Error: No se puede dividir por cero.");
        } else {
            System.out.println("La división es: " + (num1 / num2));
        }

        System.out.println("Precione ENTER para continuar");
        empanada.nextLine();
    }

    private static void modulo(Scanner lulada) {
        System.out.println("\n    MODULO");
        var num1 = leerEntero(lulada, "Ingrese el primer operador: ");
        var num2 = leerEntero(lulada, "Ingrese el segundo operador: ");

        System.out.println("El modulo es: " + (num1 % num2));

        System.out.println("Precione ENTER para continuar");
        lulada.nextLine();
    }
}
