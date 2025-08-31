package com.indigo;

public class Gerente extends Empleado {
    private String departamento;

    public Gerente(String nombre, double salario, int edad, String departamento) {
        super(nombre, salario, edad);
        this.departamento = departamento;
    }

    @Override
    public String toString() {
        return "Gerente{" +
        "departamento='" + departamento + '\'' +
        "} " + super.toString();
    }

    
    
}
