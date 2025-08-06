package model;

public class MenuItem {
    private String name;
    private Double price;

    private Menu menu;

    public MenuItem(Menu menu, String name, Double price) {
        this.name = name;
        this.price = price;
        this.menu = menu;
    }

    public String getName() {
        return name;
    }

    public Double getPrice() {
        return price;
    }

    public Menu getMenu() {
        return menu;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    

}
