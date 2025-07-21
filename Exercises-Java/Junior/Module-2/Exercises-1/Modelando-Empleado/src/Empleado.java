import java.util.Scanner;
import java.util.UUID;

public class Empleado {
    // ATRIBUTOS
    private String nombreCompleto;
    private final UUID idEmpleado = UUID.randomUUID(); // final: No se podra cambiar
    private Double salarioMensual;
    private String departamento;
    Scanner sc = new Scanner(System.in);

    // CONSTRUCTORES
    public Empleado(String nombreCompleto, String departamento) {
        this(nombreCompleto, 0.0, departamento);
    }

    public Empleado(String nombreCompleto, Double salarioMensual, String departamento) {
        this.nombreCompleto = nombreCompleto;
        this.salarioMensual = salarioMensual;
        this.departamento = departamento;
    }

    // GETTERS
    public String getNombreCompleto() {
        return nombreCompleto;
    }

    public String getIdEmpleado() {
        return idEmpleado.toString();
    }

    public Double getSalarioMensual() {
        return salarioMensual;
    }

    public String getDepartamento() {
        return departamento;
    }

    // SETTERS
    public void setSalarioMensual(Double salarioMensual) {
        if (salarioMensual < 0) {
            System.out.println("Error: el sueldo no puede tener valores negativos");
            return;
        } else {
            this.salarioMensual = salarioMensual;
        }
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    // METODOS
    public String mostrarInformacion() {
        return String.format("Nombre: %s, ID: %s, salario: %,.2f, departamento: %s", getNombreCompleto(),
                getIdEmpleado(), getSalarioMensual(), getDepartamento());
    }

    public void calcularSalarioAnual() {
        if (salarioMensual == 0) {
            System.out.printf("El empleado %s aún no tiene sueldo establecido%n", nombreCompleto);
        } else {
            Double anual = salarioMensual * 12;
            System.out.printf("Salario anual del empleado %s: %,.2f %n", nombreCompleto, anual);
        }

    }

}
