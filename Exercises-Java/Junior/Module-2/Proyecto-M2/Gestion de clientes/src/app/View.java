package app;

import java.util.Scanner;

import model.GestionUsers;

public class View {
    Scanner sc = new Scanner(System.in);

    public void menudeInicio() {
        System.out.println("----- BIENVENIDO -----\n");
        System.out.println("1. Inicio de sesión");
        System.out.println("2. Continuar como invitado");
        System.out.print("Ingrese una opcion: ");
        int opcion = sc.nextInt();
        sc.nextLine();

        switch (opcion) {
            case 1:
                System.out.println("\nINICIO DE SESIÓN");
                GestionUsers.login();                
                break;
            case 2:
                //TODO
                break;
        
            default:
                break;
        }


    }

}
