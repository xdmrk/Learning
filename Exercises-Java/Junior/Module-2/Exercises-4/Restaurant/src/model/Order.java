package model;

public class Order {
    private Integer orderNumber;
    private OrderStatus status;
    private Table table;

    // Order contiene a OrderItem
    private OrderItem[] orderItems;

    public Order(Table table, OrderItem[] orderItems) {
        this(table, OrderStatus.PENDING, orderItems);
    }

    public Order(Table table, OrderStatus status, OrderItem[] orderItems) {
        this.orderNumber = 1; // FIXME: alfo que hice y esta mal
        this.status = status; //TODO: por hacer
        this.orderItems = orderItems;
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

}
