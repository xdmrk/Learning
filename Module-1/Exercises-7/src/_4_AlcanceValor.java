import java.util.Scanner;

public class _4_AlcanceValor {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);

        System.out.print("Ingre el nombre del usuario: ");
        var nombre = scanner.nextLine();
        System.out.print("Ingre el apelldio del usuario: ");
        var apellido = scanner.nextLine();

        imprimaNombreCompleto(nombre, apellido);

        scanner.close();        
        cicloFori();
    }


    public static void imprimaNombreCompleto(String nombre, String apellido) {
        nombre = nombre.toLowerCase();//Todo en minuscula
        apellido = apellido.toUpperCase();//Todo a mayusculas

        System.out.printf("%s, %s%n", apellido, nombre); //%n es como un \n
        System.out.printf("%s, %s", apellido, nombre);
    }


    public static void cicloFor(){
        int i = 0; 

        for(; i < 10; i++) {
            System.out.println("Primer for");
        }

        for(; i < 10; i++) {
            System.out.println("Segundo for"); //Nunca se imprimiria 2°for porque cuando salga del 1°for, i = 10 y no cumpliria la condicion 
        }

        for(i = 0; i < 10; i++) {
            System.out.println("Tercer for"); //Se imprimiria el 3°for ya que se le reasigno para este for un valor a i = 0
        }

    }


    public static void cicloFori(){
        int i;// si la declaro vacia el valor de i saldra del for

        for(i = 0; i < 10; i++) {
            System.out.println("Primer for" + i);
        }

        for(; i < 11; i++) {
            System.out.println("Segundo for" + i); 
        }

        for(i = 8; i < 10; i++) { // A menos que se lo reasigne
            System.out.println("Tercer for" + i); 
        }

    }
    
}
