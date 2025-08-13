package model;

public class User {
    private String name;
    private String lastName;
    private Integer id;
    private String username;
    private String password;
    private Rol rol;
    private History[] history;

    public static int contador = 1;

    public User(String name, String lastName, String username, String password) {
        this.name = name;
        this.lastName = lastName;
        this.username = username;
        this.password = password;
        this.rol = Rol.STANDARD;
        this.id = contador;
        contador++;
    }

    public User(String name, String lastName, Integer id, String username, String password, Rol rol) {
        this.name = name;
        this.lastName = lastName;
        this.username = username;
        this.password = password;
        this.rol = rol;
        this.id = contador;
        contador++;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public Integer getId() {
        return id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public History[] getHistory() {
        return history;
    }

    public Rol getRol() {
        return rol;
    }

    public void setRol(Rol rol) {
        this.rol = rol;
    }

}
