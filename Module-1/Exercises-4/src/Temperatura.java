import java.util.Scanner;

public class Temperatura {
    public static void main(String[] args) {
        //Programa que convierta una temperatura dada en grados Celsius a gradis F y K
        var scanner = new Scanner(System.in);

        System.out.print("Ingrese la temperatura en grados Celcius: ");
        var celcius = scanner.nextDouble();
        var fahrenheit = celcius * 9 / 5 + 32;
        /* CASTING
         * fahrenheit (implicito) = Double ya que es de mayor tamaño que int, pasaria los enteros a double y el resultado seria double
         * 
         * var fahrenheit = (int)celcius * 9 / 5 + 32;
         * (explicito) al pasar la variable double a int todo se operaria entre int  
         * 
         * var fahrenheit = (int) (celcius * 9 / 5 + 32);
         * (explicito) operaria en tipo de dato Double y el resultado lo pasaria a int (f(d= 9.8) ; f(i=9)) 
         * 
         * ERROR
         * var fahrenheit = celcius * (9 / 5) + 32;
         * (9 / 5) = 1, esto porque son tipo int y devuelve asi mismo un int, pierde toda la parte decimal para multiplicar, para arreglarlo declaramos uno de los datos Double
         * var fahrenheit = celcius * (9.0 / 5) + 32;
         * el double al operarce con un int daria como resultado un double al ser mas grande
         */

         var kelvin = celcius + 273.15;

         System.out.printf("%,.2f grados Celsius son %,.2f grados Fahrenheit%n", celcius, fahrenheit);
         System.out.printf("%,.2f grados Celsius son %,.2f grados Kelvin%n", celcius, kelvin);

         scanner.close();
    }
}
