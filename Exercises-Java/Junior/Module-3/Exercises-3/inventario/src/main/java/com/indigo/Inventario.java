package com.indigo;

import java.util.HashMap;
import java.util.Map;

public class Inventario {
    private Map<String, Producto> productos = new HashMap<>();

    public void agregarProducto(Producto producto) {
        productos.put(producto.getNombre(), producto);
    }

    public void procesarProducto(String nombre, int cantidad) throws ProductoNoEncontradoException {
        Producto producto = productos.get(nombre);
        if (producto == null) {
            throw new ProductoNoEncontradoException("Producto no encontrado " + nombre);
        }
        producto.reducirCantidad(cantidad);
    }
}
