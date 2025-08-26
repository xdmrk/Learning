package com.indigo;

public class ProductoNoEncontradoException extends Exception { //checked
    
    public ProductoNoEncontradoException(String message) {
        super(message);
    }
}
