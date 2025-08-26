package com.indigo;

public class StockInsuficioenteException extends RuntimeException { //in checked

    public StockInsuficioenteException(String message) {
        super(message);
    }

}
