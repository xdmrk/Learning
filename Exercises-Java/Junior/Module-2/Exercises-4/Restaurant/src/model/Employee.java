package model;

public class Employee {
    private String name;
    private Restauran restauran;

    public Employee(String name, Restauran restauran) {
        this.name = name;
        this.restauran = restauran;
    }

    public Restauran getRestauran() {
        return restauran;
    }

    public void setRestauran(Restauran restauran) {
        this.restauran = restauran;
    }

    public String getName() {
        return name;
    }
    


}
