package model;

public class Restauran {
    private String name;
    private String address;
    private Table[] tables;
    private Menu menu;
    private Employee[] employees;


    public Restauran(String name, String address, Table[] tables, Menu menu, Employee[] employees) {
        this.name = name;
        this.address = address;
        this.tables = tables;
        this.menu = menu;
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


    public Menu getMenu() {
        return menu;
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
        menu.displayItems();
    }

    public Table findTable(int tableNumber){
        for (int i = 0; i < tables.length; i++) {
            if(tables[i] != null && tables[i].getTableNumber() == tableNumber) { // o .equals(tableNumber), ya que es un Integer a int
                return tables[i];
            }
        }
        return null;
    }


    


    
}
