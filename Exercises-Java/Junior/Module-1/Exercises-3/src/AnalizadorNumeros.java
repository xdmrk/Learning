import java.util.Scanner;

public class _2_AnalizadorNumeros {
    public static void main(String[] args) { //Estructur basica de la clase 
        Scanner entrada = new Scanner(System.in); // Objeto para leer entradas del usuario
        int opcion, numero;

        do{ //Muestre al menos una vez el menú
            System.out.println("\n¡¡ MENÚ !!");
            System.out.println("1. Analizar un solo número");
            System.out.println("2. Generar secuencia de números");
            System.out.println("0. Salir");
            System.out.print("Ingrese una opcion: ");
            opcion = entrada.nextInt(); // Toma de opcion (usuario)

            switch (opcion) { // Case por opcion registrada
                case 1: //positivo, par, <>=100.
                    System.out.print("Ingrese un numero: ");
                    numero = entrada.nextInt();
                    System.out.println(" ");

                    //Primer bloque de validacion
                    if (numero < 0){
                        System.out.printf("El numero %d es negativo", numero);
                    }else if (numero > 0){
                        System.out.printf("El numero %d es positivo", numero);
                    }else{
                        System.out.printf("El numero %d es nulo", numero);
                    }

                    //Segundo bloque de validacion (operadr ternario ?)
                    String parImpar = (numero % 2 == 0) ? ", par y" : ", impar y";
                    System.out.println(parImpar);

                    //Tercer bloque de validacion
                    if (numero < 100){
                        System.out.print(" es menor que 100\n\n");
                    }else if (numero > 100){
                        System.out.print(" es mayor que 100\n\n");
                    }else{
                        System.out.print(" es igual a 100\n\n");
                    }                                    
                    break; // Rompe el switch
            
                case 2:
                    String pOi;

                    System.out.print("Ingrese el numero de inicio: ");
                    int nI = entrada.nextInt();
                    System.out.print("Ingrese el numero de finalización: ");
                    int nF = entrada.nextInt();
                    System.out.print("Desea ver solo los numeros pares o los impares: ");

                    entrada.nextLine(); // Limpiamos el buffer o no registra la variable pOi
                    //.replaceAll: elimina espacios en blanco (espacios, tabs, saltos de línea, etc.) // +: uno o mas
                    //toLowerCase(): convierte a minuscula
                    pOi = entrada.nextLine().toLowerCase().replaceAll("\\s+", "");

                    for (int i = nI; i <= nF; i++){ // Para                 
                        if (pOi.equals("par") || pOi.equals("pares")){
                            if (i % 2 == 0){ // Que solo entren los pares
                                System.out.print(i);
                                System.out.print(" ");
                            }else{
                                continue; // Si no es par que salte a la sigiente iteracion
                            }
                        }else if(pOi.equals("impar") || pOi.equals("impares")){
                        // equals(): compara String ya que == solo compara numeros o primitivos
                            if(i % 2 != 0){ // Que solo entren los impares
                                System.out.print(i);
                                System.out.print(" ");
                            }else{
                                continue; // Si no es par que salte a la sigiente iteracion
                            }                                    
                        }else{ //Entra si no ingresa una opcion valida en nI, nF o pOi
                            System.out.println("Debe ingresar si desea ver los pares o los impares");
                            break; // Devuelve al menu principal
                        }
                    }                       
                default: // Cualquier otra opcion
                    System.out.printf("%d no es una opcion valida", opcion);                     
                    continue; // Regresa al menú
            }            
        }while(opcion != 0); // Mientras este entre las opciones, se repetira
        System.out.println("Saliendo del programa...."); // Mensaje al salir del programa
        entrada.close(); // Cerramos el scanner        
    }
}
