import java.util.Scanner;

public class _1_MenuCondicionalesBucles {
    public static void main(String[] args) {       
        int opcion, menu1; //Se declaran las variables para el menu y el sub menu
        Scanner entrada = new Scanner(System.in);
        
        do { //Bloque de codigo a ejecutar 
            // Mostrar menú
            System.out.println("\n¡¡  MENú MATEMATICO  !!");
            System.out.println("1. Calcular área de una figura");
            System.out.println("2. Calcular edad futura");
            System.out.println("3. ¿Sí es numero primo?");
            System.out.println("0. Salir\n");

            System.out.print("Ingrese una opcion valida: "); //Ingreso de la opcion (usuario)
            opcion = entrada.nextInt();

            //Opciones
            switch (opcion) {
                case 1:
                    do { //Sub menú
                    System.out.println("\nCALCULAR EL ÁREA DE UNA FIGURA");
                    System.out.println("1. Cuadrado");
                    System.out.println("2. Romboide");
                    System.out.println("3. Circulo");
                    System.out.println("4. Rectangulo");
                    System.out.println("0. Salir");
                            
                    System.out.print("\nIngrese una opcion valida: "); //Ingreso de la opcion (usuario) menu/opc1
                    menu1 = entrada.nextInt();

                    //Double area, lado, base, altura, radio; //Variables para calculos

                    //Opciones menu/opc1
                    switch (menu1) {
                        case 1:                        
                            System.out.println("\nArea de un cuadrado");
                            System.out.print("Ingrese el valor del lado: ");
                            Double lado = entrada.nextDouble(); //Toma y asigmacion de datos a variables

                            var area = lado * lado;
                            System.out.printf("El area del cuadrado de lados %.2f es: %.2f\n", lado, area); //Print format
                            break; //Se devuelve

                        case 2:
                            System.out.println("\nArea de un romboide");
                            System.out.print("Ingrese el valor de la base: ");
                            Double base = entrada.nextDouble();
                            System.out.print("Ingrese el valor dela altura: ");
                            Double altura = entrada.nextDouble();

                            area = base * altura;
                            System.out.printf("El area del romboide de base %.2f y altura %.2f es: %.2f\n", base, altura, area);
                            break; //Se devuelve

                        case 3:
                            System.out.println("\nArea de un circulo");
                            System.out.print("Ingrese el valor del radio: ");
                            Double radio = entrada.nextDouble();

                            area = radio * 3.14 ; //3.14 se toma como valor de pi
                            System.out.printf("El area del circulo de radio %.2f es: %.2f\n", radio, area);
                            break; //Se devuelve

                        case 4:
                            System.out.println("\nArea de un rectangulo");
                            System.out.print("Ingrese el valor de la base: ");
                            base = entrada.nextDouble();
                            System.out.print("Ingrese el valor dela altura: ");
                            altura = entrada.nextDouble();

                            area = base * altura;
                            System.out.printf("El area del rectangulo de base %.2f y altura %.2f es: %.2f\n", base, altura, area);
                            break; //Se devuelve

                        case 0:
                            break;
                    
                        default:
                            System.out.println("Opcion incorrecta,");
                            break; //Se devuelve
                    }

                    } while (menu1 > 0 && menu1 < 5); //Condicion = true: rerpetira el bloque // false: sale del bucle
                    break; //Para cerrar el ciclo del menu/opc1, si toma el case2: CALCULAR EDAD FUTURA

                case 2:
                    System.out.println("\nCALCULAR EDAD FUTURA");
                    System.out.print("Ingrese su edad: ");
                    int edad = entrada.nextInt();
                    System.out.print("Ingrese el año futuro a consultar: ");
                    int año = entrada.nextInt();

                    int añoFuturo;
                    añoFuturo = año - 2025;
                    edad += añoFuturo;

                    System.out.printf("Del año 2025 al año %d habran pasado %d años y tendra %d años\n", año, añoFuturo, edad);                                        
                    break; //Se devuelve

                case 3:
                    System.out.println("\n¿Sí ES NUMERO PRIMO?");
                    System.out.print("Ingrese su numero a consultar: ");
                    int numero = entrada.nextInt();

                    if(numero > 1){ //Si es mayor que 1
                        for(int i = 2; i <= numero; i++){
                            if(numero % i == 0 && i < numero){ // modulo = 0 y numero sea mayor que i
                                System.out.println("El "+numero+ " no es numero primo ya que es divisible por "+i);
                                break;
                            }if(i == numero){ // Si i toma el valor de {numero}
                                System.out.println("El numero "+numero+" es primo");
                                break;                                
                            }
                        }
                    }else{ // Tomaria los numeros <= 1
                        System.out.println("El "+numero+ " no es numero primo");
                    }            
                default: // Del do (opciones)
                    break; //Sale
            }
        } while (opcion > 0 && opcion < 4); //Condicion = true: rerpetira el bloque // false: sale del bucle 

        entrada.close(); //Cerramos el scanner
    }
}
