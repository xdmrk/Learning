public class Client extends Person {
    private String contactPhone;

    public Client(String name, Integer age, String contactPhone) {
        super(name, age);
        this.contactPhone = contactPhone;
    }

    public String getContactPhone() {
        return contactPhone;
    }

    public void setContactPhone(String contactPhone) { // setter ya que el cliente podria cambiar de numero
        this.contactPhone = contactPhone;
    }

    @Override
    public void mostrarDatos() {
        System.out.printf("Cliente: nombre: %s, edad: %d, telefono de contacto: %s%n", getName(), getAge(), getContactPhone());
    }
    
}
