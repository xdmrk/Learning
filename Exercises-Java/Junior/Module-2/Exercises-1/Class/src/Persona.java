public class Persona {
    // ATRIBUTOS
    private String firsName;
    private String lastName;
    private String email;
    private String phoneNumber;

    // CONSTRUCTORES > source action > Generate constructors
    // Procurar que todos los atributos del objeto esten inicializados
    public Persona() {
        this("Sin nombre", "Sin apellido"); // this: llama al constructor que recibe dos argumentos
    }

    public Persona(String firsName, String lastName) {
        this(firsName, lastName, "Sin email");
    }

    public Persona(String firsName, String lastName, String email) {
        this(firsName, lastName, email, "Sin numero");
    }

    public Persona(String firsName, String lastName, String email, String phoneNumber) {
        this.firsName = firsName;
        this.lastName = lastName;
        this.email = email;
        this.phoneNumber = phoneNumber;
    }

    // METODOS GETTERS
    public String getFirsName() {
        return firsName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getEmail() {
        return email;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    // METODOS SETTERS
    public void setEmail(String email) {
        this.email = email;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    // METODO TOSTRING()
    @Override
    public String toString() {
        return String.format("Nombre: %s, apellido: %s, email: %s, numero: %s", firsName, lastName, email, phoneNumber);
    }

}
