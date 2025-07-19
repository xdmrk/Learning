import java.util.Scanner;

public class Salida {

    public static void saalida(){
        Scanner sc = new Scanner(System.in);

        System.out.print("Introduzca palabra 1: ");
        String palabra1 = sc.nextLine();
        
        System.out.print("Introduzca palabra 2: ");
        String palabra2 = sc.nextLine();
        
        System.out.print("Introduzca palabra 3: ");
        String palabra3 = sc.nextLine();

        System.out.println(palabra1 + " " + palabra2 + " " + palabra3 + " ");
        
        sc.close();
    }
    
}
