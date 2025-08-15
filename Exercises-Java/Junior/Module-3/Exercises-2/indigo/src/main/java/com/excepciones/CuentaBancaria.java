package com.excepciones;

public class CuentaBancaria {
    private double saldo;

    public CuentaBancaria(double saldoInicial) {
        this.saldo = saldoInicial;
    }

    public void Retirar(double monto) throws SaldoInsuficienteExecption {
        if(monto > saldo) {
            throw new SaldoInsuficienteExecption("Saldo insuficiente"); //Bombillo: Add thorws declaration: modifica la firma

        }
        saldo -= monto;
        System.out.println("Retiro exitoso");
    }

    

}
