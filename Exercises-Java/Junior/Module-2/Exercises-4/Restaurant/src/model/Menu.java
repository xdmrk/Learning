package model;

public class Menu {
    private String name;
    private Restauran restauran;
    private MenuItem[] menuItems;


    public Menu(String name, Restauran restauran, MenuItem[] menuItems) {
        this.name = name;
        this.restauran = restauran;
        this.menuItems = menuItems;
    }


    public String getName() {
        return name;
    }


    public Restauran getRestauran() {
        return restauran;
    }


    public MenuItem[] getMenuItems() {
        return menuItems;
    }


    public void setName(String name) {
        this.name = name;
    }

    public void addMenuItem(MenuItem menuItem) {
        // TODO
    }

    public void removeMenuItem(MenuItem menuItem) {
        // TODO 
    }
    
    public void displayItems(){
        for (int i = 0; i < menuItems.length; i++) {
            System.out.println(menuItems{i});
            
        }
    }
    

}
