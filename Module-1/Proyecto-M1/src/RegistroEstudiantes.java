import java.util.Scanner;

public class RegistroEstudiantes {
    // Variables estáticas (compartidas por todos los metodos static de la clase)
    static String nombre = null;
    static Double nota1 = -1d;
    static Double nota2 = 0d;
    static Double nota3 = 0d;
    static Double promedio = 0d;

    public static void main(String[] args) { // punto de entrada del programa
        var sc = new Scanner(System.in); // Importamos Scanner
        mostrarMenu(sc); // Llamamos el metodo para el menú

        sc.close(); // cerramos el scanner
    }

    public static void mostrarMenu(Scanner sc) { // Debemos pasar el Scanner como parametro ya que esta en el main y
                                                 // deseamos traerlo
        int opcion; // Decalramos la variable afuera para que no quede encerrada en el do
        boolean salir = false;

        do { // Muestre al menos una vez
             // No se debe limpiar el buffer al iniciar
            System.out.println("SISTEMA DE REGISTRO DE ESTUDIANTES");
            System.out.println("--------------------------------------------");
            System.out.println("""
                    1. Registrar datos de un estudiante
                    2. Mostrar datos del estudiante actual
                    3. Calcular promedio de notas del estudiante actual
                    4. Validar nota
                    5. Validar nombre
                    0. Salir
                    """);
            System.out.print("Ingrese su opcion: ");
            opcion = sc.nextInt(); // Registro de opcion del usuario
            sc.nextLine();

            switch (opcion) {
                case 1:
                    registroEstudiantes(sc);
                    break;

                case 2:
                    mostrarInformacion();
                    break;

                case 3:
                    System.out.println(calcularPromedio(sc));
                    break;

                case 4:

                    break;

                case 5:

                    break;

                case 0:
                    salir = true;
                    break;

                default:
                    System.out.println("Opcion invalida");
                    break;
            }
            System.out.print("Precione ENTER para continuar "); // debe precionar Enter antes de volver a ver el menu
            sc.nextLine();

        } while (!salir); // Mientras no sea 0, repetir el menú
        System.out.println("Hasta pronto...");

    }

    private static void registroEstudiantes(Scanner sc) {
        // String nombre = ""; //var no permite variables vacias
        // Double nota1, nota2, nota3; //var no permite inicializar varias variables en
        // una sola linea

        System.out.println("REGISTRO -----------------------------------");
        validarNombre(sc);
        // System.out.print("Ingrese la primera nota del estudiante: ");
        // nota1 = sc.nextDouble();
        // System.out.print("Ingrese la segunda nota del estudiante: ");
        // nota2 = sc.nextDouble();
        // System.out.print("Ingrese la tercera nota del estudiante: ");
        // nota3 = sc.nextDouble();

        nota1 = validarNota("primera", sc);
        nota2 = validarNota("segunda", sc);
        nota3 = validarNota("tercera", sc);
        sc.nextLine(); // si no se limpiar el buffer salta el precionar ENTER
    }

    private static void mostrarInformacion() {
        if (nombre.equals("")) {
            System.out.println("Sin registros\n");
            return;
        }
        System.out.println("DATOS DEL ESTUDIANTE-------------------------");
        System.out.println("Nombre: " + nombre);
        System.out.println("Primera nota: " + nota1);
        System.out.println("Segunda nota: " + nota2);
        System.out.println("Tercera nota: " + nota3);
    }

    private static Double calcularPromedio(Scanner sc) {
        var promedio = (nota1 + nota2 + nota3) / 3;
        System.out.println("PROMEDIO -----------------------------------");
        if (nota1 == -1) {
            System.out.println("Sin notas\n");
            mostrarMenu(sc);
        }
        return promedio; // retorna el promedio

    }

    private static Double validarNota(String mensaje, Scanner sc) {
        // boolean valido = false;
        // else{
        // valido = true;
        // return nota;
        // }while(!valido); --> No se puede ya que no retornaria nunca

        do {
            System.out.print("Ingrese la " + mensaje + " nota del estudiante: ");
            Double nota = sc.nextDouble();

            if (nota < 0) {
                System.out.println("La nota no puede ser un valor negativo\n");
            } else if (nota >= 10) {
                System.out.println("La nota no puede tener un valor mayor a 10\n");
            } else {
                return nota;
            }

        } while (true);

    }

    private static boolean validarNombre(Scanner sc) {
         
        do{
            System.out.print("Ingrese el nombre completo del estudiante: ");
                String validacion = sc.nextLine();

            if (validacion == null || validacion.trim().isEmpty()) {
                System.out.println("Error: El nombre no puede estar vacío");
                //.trim(): Elimina espacios en blanco al inicio y final   |   .isEmpty(): Verifica si la cadena está vacía
                
            } else {
                nombre = validacion.trim(); 
                return true;
            }
        }while(true);
        
        
    }
}
