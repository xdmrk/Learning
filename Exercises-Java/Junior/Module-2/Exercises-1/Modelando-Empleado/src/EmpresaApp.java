public class EmpresaApp {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Astro", "Ventas");
        Empleado empleado2 = new Empleado("Felipe", 2000000d, "RRH");
        Empleado empleado3 = new Empleado("Maria", "Facturacion");
        Empleado empleado4 = new Empleado("Camilo", "Ventas");
        Empleado empleado5 = new Empleado("Perla", 3000000d,"Gerente");

        System.out.println(empleado1.mostrarInformacion());
        System.out.println(empleado2.mostrarInformacion());
        System.out.println(empleado3.mostrarInformacion());
        System.out.println(empleado4.mostrarInformacion());
        System.out.println(empleado5.mostrarInformacion());
    

        empleado2.setSalarioMensual(-7d);
        empleado3.setSalarioMensual(2500000d);
        empleado1.setDepartamento("Supervisor");

        System.out.println(empleado1.mostrarInformacion());
        System.out.println(empleado2.mostrarInformacion());
        System.out.println(empleado3.mostrarInformacion());
        System.out.println(empleado4.mostrarInformacion());
        System.out.println(empleado5.mostrarInformacion());

        //empleado1.nombreCompleto = "sjdhjsahdkjs" error al ser privado
        empleado1.calcularSalarioAnual();
        empleado2.calcularSalarioAnual();
        empleado3.calcularSalarioAnual();
        empleado4.calcularSalarioAnual();
        empleado5.calcularSalarioAnual();
    }
}
