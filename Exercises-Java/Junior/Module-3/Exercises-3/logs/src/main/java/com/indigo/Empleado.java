package com.indigo;

import org.apache.logging.log4j.*;

public class Empleado {
    private static final Logger logger = LogManager.getLogger(Empleado.class);

    //Atributos
    private String nombre;
    private double salario;
    private int edad;


    public Empleado(String nombre, double salario, int edad) {
        this.nombre = nombre;
        this.salario = salario;
        this.edad = edad;

        if(edad < 18) {
            logger.warn("El empleado " + nombre + " es menor de edad");
        }
    }

    //aumentar salario
    public void aumentarSalario(double cantidad) {
        this.salario += cantidad;
    }

    @Override
    public String toString() {
        return "Empleado{" +
        "nombre='" + nombre + '\'' +
        ", edad=" + edad +
        ", salario=" + salario +
        '}';
    }

    

}
