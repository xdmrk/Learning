# Operador Ternario (`? :`) 
###### *[Ejercicio](Module-1/Exercises-6/src/_1_Ternario.java)*

Es una forma concisa de escribir un `if-else` simple que **devuelve un valor**. Su sintaxis es: `condicion ? valor_si_true : valor_si_false;`. Es útil para asignaciones simples basadas en una condición.

* **`condición`**: Expresión booleana que se evalúa (true o false).
* **`valor_si_verdadero`**: Se retorna/ejecuta si la condición es true.
* **`valor_si_falso`**: Se retorna/ejecuta si la condición es false.

```Java
//Ejemplo 1
int num = 20;
String mensaje;

// Usando if-else:
if (num % 2 == 0) {
    mensaje = "Par";
} else {
    mensaje = "Impar";
}
System.out.println(mensaje); // Salida: Par

int num = 10;
String tipoNumero = (num % 2 == 0) ? "Par" : "Impar"; // Usando el operador ternario (equivalente al if-else anterior):
System.out.println("El número es: " + tipoNumero); // Salida: El número es: Par

//Ejemplo 2
int edadUsuario = 25;

String grupoEdad = (edadUsuario < 13) // Ternario anidado 
    ? "Niño" 
    : (edadUsuario < 18) // La negacion de la condicion ternaria puede ser otra condicion
        ? "Adolescente" 
        : (edadUsuario < 65) 
            ? "Adulto" 
            : "Adulto mayor";

System.out.println("Grupo de edad: " + grupoEdad); // Salida: Grupo de edad: Adulto
```

## ¿Cuándo usarlo?
1. **Decisiones simples**: Reemplaza `if-else` cortos (1 condición, 2 resultados).
2. **Asignaciones condicionales**: Ideal para inicializar variables.
3. **Expresiones en métodos**: Útil en `return` o argumentos de métodos.
  ```Java
  public String saludo(boolean esMañana) {
      return esMañana ? "Buenos días" : "Buenas tardes";
  }
  ```

## ¿Cuándo evitarlo?
1. **Condiciones complejas**: Si hay múltiples `if-else` anidados, usa `if` tradicional.
2. **Código crítico**: Si la legibilidad se ve afectada, prioriza claridad sobre brevedad.

