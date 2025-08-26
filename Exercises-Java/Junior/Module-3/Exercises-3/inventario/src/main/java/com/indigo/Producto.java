package com.indigo;

public class Producto {
    private String nombre;
    private int cantidad;

    public Producto(String nombre, int cantidad) {
        this.nombre = nombre;
        this.cantidad = cantidad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void reducirCantidad(int cantidad) {
        if (this.cantidad < cantidad) {
            throw new StockInsuficioenteException("Stock insuficiente para el producto " + getNombre());
        }
        this.cantidad -= cantidad;
    }

}
