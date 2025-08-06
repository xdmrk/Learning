package model;

public class Table {
    private Integer tableNumber;
    private Integer capacidad;
    private Boolean occupied;
    private Restauran restaurant;
    private Order actualOrder;

    public Table(Integer tableNumber, Integer capacidad, Restauran restaurant){
        this.occupied = false;
        this.capacidad = capacidad;
        this.restaurant = restaurant;
        this.tableNumber = tableNumber;
    }

    public Integer getTableNumber() {
        return tableNumber;
    }

    public Integer getCapacidad() {
        return capacidad;
    }

    public void setOccupied(Boolean occupied) {
        this.occupied = occupied;
    }
    public void setRestaurant(Restauran restaurant) {
        this.restaurant = restaurant;
    }

    

    




}
