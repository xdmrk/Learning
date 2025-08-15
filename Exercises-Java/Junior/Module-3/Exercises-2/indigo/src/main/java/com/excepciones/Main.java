package com.excepciones;

import java.io.FileNotFoundException;
import java.io.FileReader;

public class Main {
    public static void main(String[] args) throws SaldoInsuficienteExecption {
        CuentaBancaria cuenta = new CuentaBancaria(100);

        cuenta.Retirar(20); //Bombillo

    }

    private static void ejemplo1() {
        int a = 12;
        int b = 0;

        System.out.println(a / b);
        /*
         * Exception in thread "main" java.lang.ArithmeticException: / by zero
         * at com.excepciones.Main.main(Main.java:8)
         * ERROR en tiempo de ejecucion
         */
        System.out.println("Fin del programa");
    }

    private static void ejemplo2() {
        String texto = "abc";
        int numero = Integer.parseInt(texto);
        /*
         * Exception in thread "main" java.lang.NumberFormatException: For input string:
         * "abc"
         * at java.base/java.lang.NumberFormatException.forInputString(
         * NumberFormatException.java:67)
         */

        FileReader archivo = new FileReader("texto.txt");
        /*
         * Unhandled exception type FileNotFoundException
         * execption sin manejar
         */
    }

    private static void ejemplo3() {
        
        try {
            String texto = "abc";
            int numero = Integer.parseInt(texto);

            int resultado = 10/0;

            int[] arreglo = {1,2,3};
            System.out.println(arreglo[5]);

            FileReader archivo = new FileReader("texto.txt");

        } catch (NumberFormatException a) {
            /*Primer error de integer.parseInt */
            System.out.println("Error en el formato del numero" + a.getMessage());
        } catch (ArithmeticException e) {            
            System.out.println("Error de division por cero");
        } catch (ArrayIndexOutOfBoundsException e) {            
            System.out.println("Indice fuera de los limites del arreglo");
        } catch (Exception e) {  //clase padre  
            System.out.println("Archivo no encontrado");
        }
        
    }
}