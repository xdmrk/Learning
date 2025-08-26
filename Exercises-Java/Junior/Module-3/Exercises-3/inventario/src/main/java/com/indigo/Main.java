package com.indigo;

public class Main {
    public static void main(String[] args) {
        Inventario inventario = new Inventario();

        inventario.agregarProducto(new Producto("Laptop", 10));
        inventario.agregarProducto(new Producto("Mouse", 8));
        inventario.agregarProducto(new Producto("Cargador", 4));
        inventario.agregarProducto(new Producto("Tablet", 15));

        try {
            inventario.procesarProducto("Laptop", 10);
            inventario.procesarProducto("Mouse", 10);
            inventario.procesarProducto("Cargador", 3);
            inventario.procesarProducto("Tablet", 11);
            inventario.procesarProducto("Camara", 11);
        } catch (ProductoNoEncontradoException | StockInsuficioenteException e) {
            System.out.println(e.getMessage());
        }
    }
}