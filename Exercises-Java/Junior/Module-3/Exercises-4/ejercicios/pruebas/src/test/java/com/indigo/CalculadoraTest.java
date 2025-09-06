package com.indigo;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

public class CalculadoraTest {
    @Test
    void testSuma() {
        Calculadora calc = new Calculadora();
        assertEquals(5, calc.sumar(2, 3));
    }
    @Test
    void testResta() {
        Calculadora calc = new Calculadora();
        assertEquals(0, calc.restar(2, 3));
    }
    @Test
    void testDivi() {
        Calculadora calc = new Calculadora();
        assertEquals(5, calc.dividir(10, 2));
    }
    @Test
    void testMul() {
        Calculadora calc = new Calculadora();
        assertEquals(6, calc.multiplicar(2, 3));
    }

    @Test
    void testDiviPorCero() {
        Calculadora calc = new Calculadora();
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            calc.dividir(6, 0);
        });
    }

}
