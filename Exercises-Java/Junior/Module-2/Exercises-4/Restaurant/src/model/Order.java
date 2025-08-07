package model;

public class Order {
    private Integer orderNumber;
    private OrderStatus status;
    private Table table;    
    private OrderItem[] orderItems; // Order contiene a OrderItem


    public Order(Table table, Integer orderItemsSize) {
        this.orderNumber = 1; // FIXME: algo que hice y esta mal
        this.status = OrderStatus.PENDING;
        this.orderItems = new OrderItem[orderItemsSize];
        this.table = table;
    }

    // GETTERS
    public Integer getOrderNumber() {
        return orderNumber;
    }

    public OrderStatus getStatus() {
        return status;
    }

    public OrderItem[] getOrderItems() {
        return orderItems;
    }

    public Table getTable() {
        return table;
    }

    // SETTERS
    public void setStatus(OrderStatus status) {
        this.status = status;
    }

    public void setTable(Table table) {
        this.table = table;
    }

    //METODOS
    public void addItem(OrderItem item) {
        for (int i = 0; i < orderItems.length; i++) {
            if (orderItems[i] == null) {
                orderItems[i] = item;
                return;
            }
        }
        System.out.println("La lista de items está llena");
    }

    public Double calculateTotal() {
        var total = 0d;
        for (int i = 0; i < orderItems.length; i++) {
            if (orderItems[i] != null) {
                total += orderItems[i].calculateSubtotal();
            }
        }
        return total;
    }

    public void displayDetails() {
        System.out.printf("Pedido N° %d%nEstado: %s%n", orderNumber, status);
        System.out.println("---- Productos del pedido ----");
        for (int i = 0; i < orderItems.length; i++) {
            if (orderItems[i] != null) {
                var item = orderItems[i];
                System.out.printf("Nombre: %s, Cantidad: %d, Subtotal: $ %,.2f",
                item.getMenuItem().getName(),
                item.getQuantity(),
                item.calculateSubtotal());
            }
        }
    }

}
