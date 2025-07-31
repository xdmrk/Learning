public class App {
    public static void main(String[] args) {
        // Creando empleados
        var company = new Enterprise("Beer");
        var pepe = new Directive("Pepe", 25, 10_000d, "CEO");
        

        var luisa = new Employee("Luisa", 20,1_000d);        
        luisa.setManager(pepe);

        var manuel = new Employee("Manuel", 26, 1_200d);        
        manuel.setManager(pepe);    

        
        // Agregando empleados a compañia
        company.addEmployee(0, pepe);
        company.addEmployee(1, luisa);
        company.addEmployee(2, manuel);

        // Agregando empleados a directivos
        pepe.addEmployee(0, luisa);
        pepe.addEmployee(1, manuel);

        // Creando clientes         
        var santiago = new Client("Santiago", 30, "320225455");

        // Agregando clientes a la compañia
        company.addClient(0, santiago);   
        
        System.out.println("Empleados:");
        var employees = company.getEmployees();
        for (int i = 0; i < employees.length; i++) {
            if (employees[i] != null) {
                employees[i].mostrarDatos();
            }
        }

        System.out.println("");
        
        System.out.println("Clientes:");
        var clients = company.getClients();
        for (int i = 0; i < clients.length; i++) {
            if (clients[i] != null) {
                clients[i].mostrarDatos();
            }
        }

    }
}
