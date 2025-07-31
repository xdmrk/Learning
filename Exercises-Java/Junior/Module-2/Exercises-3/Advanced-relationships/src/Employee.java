public class Employee extends Person{
    private Double salary;
    private Directive manager; // 0..1

    public Employee(String name, Integer age, Double salary) {
        super(name, age);
        this.salary = salary;
    }

    public Double getSalary() {
        return salary;
    }

    public void setManager(Directive manager) {
        this.manager = manager;
    }

    public Directive getManager() {
        return manager;
    }

    @Override
    public void mostrarDatos() {
        System.out.printf("Empleado: nombre: %s, edad: %d, salario: $ %,.2f%n", getName(), getAge(), getSalary());
    }
    
}
