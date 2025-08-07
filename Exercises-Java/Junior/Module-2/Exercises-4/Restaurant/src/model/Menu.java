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

    public void setName(String name) {
        this.name = name;
    }

    public Restauran getRestauran() {
        return restauran;
    }

    public MenuItem[] getMenuItems() {
        return menuItems;
    }

    //METODOS
    public MenuItem findItem(String itemName) { //Encontrar
        for (int i = 0; i < menuItems.length; i++) {
            if (menuItems[i] != null && menuItems[i].getName().equals(itemName)) {
                return menuItems[i];
            }

        }
        return null;
    }

    public void displayItems(){ //Mostrar
        for (int i = 0; i < menuItems.length; i++) {
            System.out.println(menuItems[i]);
        }
        
    }

}
