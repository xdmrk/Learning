import java.util.Scanner;

public class CalculadoraIMC {
    public static void main(String[] args) {
        var input = new Scanner(System.in);

        System.out.print("Ingrese el peso en kilogramos: ");
        var peso = input.nextDouble();

        System.out.print("Ingrese la altura: ");
        var altura = input.nextInt();

        var alturaMetros = altura / 100.0;

        var imc = peso / (alturaMetros * alturaMetros);

        System.out.printf("El indice de masa corporal IMC es de: %.1f%n", imc);
        input.close();
        
    }
    
}
