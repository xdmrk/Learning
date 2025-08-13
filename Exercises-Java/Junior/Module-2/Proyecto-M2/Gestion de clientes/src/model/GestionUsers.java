package model;

import java.util.Scanner;

public interface GestionUsers {
    User[] DEFAULT_USERS = new User[50]; // `public static final` por defecto
    Scanner sc = new Scanner(System.in);
    /**
     * Inicion de sesión `static`, pertenece a la interfaz misma
     */
    static User login() {
        System.out.print("Username: ");
        String inputusername = sc.nextLine();
        
        for (int i = 0; i < DEFAULT_USERS.length; i++) {
            if (DEFAULT_USERS[i] != null && inputusername.equals(DEFAULT_USERS[i].getUsername())) {
                int intentos = 3;

                while (intentos > 0) {
                    System.out.print("Password: ");
                    String inputupassword = sc.nextLine();

                    if (inputupassword.equals(DEFAULT_USERS[i].getPassword())) {
                        System.out.println("Bienvenido "+ DEFAULT_USERS[i].getUsername() + "!\n");
                        return DEFAULT_USERS[i];
                    } else { 
                        intentos--;  
                        System.out.println("Password incorrecto, quedan " + intentos + " intentos");
                    }                     
                } return null; 
            }
        } System.out.println("Usuario no encontrado");
        return null;     
    }

    /**
     * Inicion de sesión
     */
    default void addUser() {
        // TODO
    }

    /**
     * Inicion de sesión
     */
    default void deleteUser() {
        // TODO
    }

    /**
     * Inicion de sesión
     */
    default void searchUser() {
        // TODO
    }

    /**
     * Inicion de sesión
     */
    default void updateUser() {
        // TODO
    }

    /**
     * Inicion de sesión
     */
    default void modName() {
        // TODO
    }

    /**
     * Inicion de sesión
     */
    default void modPassw() {
        // TODO
    }

}
