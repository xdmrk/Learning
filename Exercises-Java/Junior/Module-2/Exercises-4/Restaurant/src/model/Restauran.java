package model;

public class Restauran {
    private String name;
    private String address;
    private Table[] tables;
    private Menu menus;
    private Employee[] employees;


    public Restauran(String name, String address, Table[] tables, Menu menus, Employee[] employees) {
        this.name = name;
        this.address = address;
        this.tables = tables;
        this.menus = menus;
        this.employees = employees;
    }


    public String getName() {
        return name;
    }


    public String getAddress() {
        return address;
    }


    public Table[] getTables() {
        return tables;
    }


    public Menu getMenus() {
        return menus;
    }


    public Employee[] getEmployees() {
        return employees;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAddress(String address) {
        this.address = address;
    }


    public void displayMenu() {
        Menu.displayItems();
    }

    


    
}
