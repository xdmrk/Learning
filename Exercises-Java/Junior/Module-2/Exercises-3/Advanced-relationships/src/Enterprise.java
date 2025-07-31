public class Enterprise {
    private String name;
    private Employee[] employees;
    private Client [] clients;    

    public Enterprise(String name) {
        this.name = name;
        this.employees = new Employee[50];
        this.clients = new Client[100];
    }

    public String getName() {
        return name;
    }

    public Client[] getClients() {
        return clients;
    }

    public Employee[] getEmployees() {
        return employees;
    }

    public void addEmployee(int index, Employee employee) {
        employees[index] = employee;
    }

    public void addClient(int index, Client client) {
        clients[index] = client;
    }
}
