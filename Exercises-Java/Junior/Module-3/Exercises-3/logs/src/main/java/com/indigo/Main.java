package com.indigo;

import org.apache.logging.log4j.*;

public class Main {

    private static final Logger logger = LogManager.getLogger(Main.class);
    public static void main(String[] args) {

        logger.info("Iniciando la app");

        //Crear empleados y gerente
        Empleado emp1 = new Empleado("Juan", 850000, 16);
        Gerente ger1 = new Gerente("Pablo", 5_000_000, 40, "Ventas");

        logger.info("Informacion del empleado: " + emp1);
        logger.info("Informacion del gerente: " + ger1);

        //Aumentar salario
        emp1.aumentarSalario(10);
        ger1.aumentarSalario(20);

        logger.info("Informacion del empleado: "+ emp1);
        logger.info("Informacion del empleado: "+ ger1);
        
    }
}