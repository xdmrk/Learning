# Clase 4: Funciones, Modularidad y Proyecto Práctico Integrador

[Funciones (Métodos): Los Bloques de Construcción](#Funciones-Métodos-Los-Bloques-de-Construcción)
 - [Declaración de Métodos (void)](#Declaración-de-Métodos-void)
 - [Parámetros y Argumentos](#Parámetros-y-Argumentos)
 - [Métodos con Retorno](#Métodos-con-Retorno)

[Alcance de Variables (Scope)](#Alcance-de-Variable-Scope)

[Diseño Modular: Dividiendo el Problema](#Diseño-Modular-Dividiendo-el-Problema)

<br> 


## Funciones (Métodos): Los Bloques de Construcción

Una **función** o **método** es un bloque de código que tiene un nombre y realiza una tarea específica. Piensa en ellos como herramientas que puedes usar varias veces en diferentes partes de tu programa sin tener que reescribir el mismo código.

**¿Por qué usar funciones?**

- **Reutilización**: Escribes el código una vez y lo llamas (**invocas**) cada vez que lo necesitas.
- **Organización**: Dividen un programa grande en partes más pequeñas y manejables.
- **Legibilidad**: El código es más fácil de leer y entender cuando las tareas están separadas en funciones con nombres descriptivos.
- **Mantenimiento**: Es más fácil encontrar y corregir errores o modificar una tarea si está encapsulada en una función.

Ya has usado un método: el método `main`. Es el punto de entrada de tu programa.

```Java
public class MiPrograma {
    // Este es el método main
    public static void main(String[] args) {
        // Código principal
    }
}
```

### Declaración de Métodos (void)

Para crear tus propias funciones, necesitas declararlas. Aquí vemos un método simple que no devuelve ningún valor (usa la palabra clave `void`) y no recibe información (no tiene **parámetros**).

```Java
public class EjemploFunciones {

    // Declaración del método saludar
    // public static: Por ahora, siempre usaremos esto para los métodos que creamos en Módulo 1
    // void: Indica que este método NO devuelve ningún valor
    // saludar: Es el nombre del método
    // (): Indica que no recibe parámetros
    public static void saludar() {
        System.out.println("¡Hola desde una función!");
    }

    public static void main(String[] args) {
        System.out.println("Antes de llamar a la función.");

        saludar(); // Llamada o invocación al método saludar()

        System.out.println("Después de llamar a la función.");
    }
}
// Salida:
// Antes de llamar a la función.
// ¡Hola desde una función!
// Después de llamar a la función.
```

### Parámetros y Argumentos

Los métodos a menudo necesitan información para realizar su tarea. Esta información se pasa a través de **parámetros**. Cuando llamas a un método, los valores que le envías se llaman **argumentos**.

- **Parámetros**: Variables declaradas en la firma del método que reciben los valores.
- **Argumentos**: Los valores reales que pasas cuando llamas al método.

  ```Java
  public class EjemploFuncionesConParametros {

      // Método que recibe un parámetro de tipo String llamado 'nombre'
      public static void saludarNombre(String nombre) {
          System.out.println("¡Hola, " + nombre + "!");
      }

      // Método que recibe dos parámetros: un String y un int
      public static void imprimirMensajeRepetido(String mensaje, int veces) {
          for (int i = 0; i < veces; i++) {
              System.out.println(mensaje);
          }
      }

      public static void main(String[] args) {
          saludarNombre("Ana"); // "Ana" es el argumento para el parámetro 'nombre'
          saludarNombre("Juan"); // "Juan" es otro argumento

          imprimirMensajeRepetido("Repetir esto", 3); // "Repetir esto" y 3 son argumentos
      }
  }
  // Salida:
  // ¡Hola, Ana!
  // ¡Hola, Juan!
  // Repetir esto
  // Repetir esto
  // Repetir esto
  ```

- **Paso por Valor (para tipos primitivos)**: Cuando pasas un tipo de dato primitivo (`int`, `double`, `boolean`, `char`, etc.) como argumento a un método, Java crea una **copia** de ese valor y la pasa al parámetro del método. Si modificas el valor del parámetro dentro del método, la variable original fuera del método **no se ve afectada**.

  ```Java
  public class PasoPorValorEjemplo {

      public static void modificarNumero(int num) {
          System.out.println("Dentro del método - Antes de modificar: " + num); // Muestra la copia
          num = num * 2; // Modifica la copia local
          System.out.println("Dentro del método - Después de modificar: " + num); // Muestra la copia modificada
      }

      public static void main(String[] args) {
          int miNumero = 10;
          System.out.println("Antes de llamar al método: " + miNumero); // Salida: 10

          modificarNumero(miNumero); // Pasamos una copia de miNumero (el valor 10)

          System.out.println("Después de llamar al método: " + miNumero); // Salida: 10 (la variable original no cambió)
      }
  }
  ```

### Métodos con Retorno

A menudo, quieres que una función no solo realice una tarea, sino que también te dé un **resultado**. Para esto, usas métodos que **devuelven un valor**. En lugar de `void`, especificas el **tipo de dato** que el método devolverá, y usas la palabra clave `return`.

```Java
public class EjemploFuncionesConRetorno {

    // Método que suma dos números enteros y devuelve el resultado (un int)
    public static int sumar(int a, int b) {
        int resultado = a + b;
        return resultado; // Devuelve el valor de 'resultado'
        // Cualquier código después de 'return' en este método NO se ejecutará
    }

    // Método que verifica si un número es par y devuelve un boolean
    public static boolean esPar(int numero) {
        return numero % 2 == 0; // Devuelve directamente el resultado de la expresión booleana
    }

    // Método que concatena dos cadenas y devuelve un String
    public static String unirCadenas(String cad1, String cad2) {
        return cad1 + " " + cad2;
    }


    public static void main(String[] args) {
        // Llamamos a sumar() y usamos el valor retornado
        int sumaTotal = sumar(5, 3);
        System.out.println("La suma es: " + sumaTotal); // Salida: La suma es: 8

        // Llamamos a esPar() y usamos el valor retornado en un condicional
        int miNumero = 4;
        if (esPar(miNumero)) {
            System.out.println(miNumero + " es un número par."); // Salida: 4 es un número par.
        }

        // Llamamos a unirCadenas() y mostramos el resultado directamente
        System.out.println(unirCadenas("Hola", "Mundo")); // Salida: Hola Mundo
    }
}
```

El tipo de dato que especificas antes del nombre del método (`int`, `boolean`, `String`, etc.) indica el tipo de valor que debes devolver usando `return`. Un método declarado como `void` no puede usar `return` para devolver un valor (solo `return;` para salir anticipadamente).

<br> 

## Alcance de Variables (Scope)

El alcance de una variable se refiere a la parte del código donde esa variable es accesible.

- **Alcance Local**: Las variables declaradas _dentro de un método_ o _dentro de un bloque_ de código específico (como el cuerpo de un `if`, `for`, `while`, etc.) tienen alcance local. Solo son visibles y utilizables desde el punto donde se declaran hasta el final del bloque en el que se encuentran.

  ```Java
  public class AlcanceLocalEjemplo {

      public static void metodo1() {
          int variableLocalMetodo1 = 10; // Alcance: solo dentro de metodo1()
          System.out.println("Dentro de metodo1: " + variableLocalMetodo1);
          // System.out.println(variableLocalMetodo2); // ERROR: variableLocalMetodo2 no es visible aquí
      }

      public static void metodo2() {
          int variableLocalMetodo2 = 20; // Alcance: solo dentro de metodo2()
          System.out.println("Dentro de metodo2: " + variableLocalMetodo2);
          // System.out.println(variableLocalMetodo1); // ERROR: variableLocalMetodo1 no es visible aquí
      }

      public static void main(String[] args) {
          int variableLocalMain = 30; // Alcance: solo dentro de main()
          System.out.println("Dentro de main: " + variableLocalMain);

          metodo1();
          metodo2();

          // System.out.println(variableLocalMetodo1); // ERROR: Fuera de alcance
          // System.out.println(variableLocalMetodo2); // ERROR: Fuera de alcance

          if (variableLocalMain > 0) {
              String mensaje = "Es positivo"; // Alcance: solo dentro de este bloque if
              System.out.println(mensaje);
          }
          // System.out.println(mensaje); // ERROR: 'mensaje' está fuera de alcance aquí
      }
  }
  ```

  Las variables locales solo existen mientras se ejecuta el método o bloque donde están declaradas.

- **Alcance de Clase (Miembros de Clase)**: Las variables declaradas directamente dentro de la clase, pero fuera de cualquier método, se llaman **variables de instancia** o **variables estáticas** (si usan `static`). Tienen un alcance más amplio y pueden ser accedidas por todos los métodos de la clase (dependiendo de su nivel de acceso, que veremos más adelante).  
Por ahora, nos enfocaremos principalmente en el alcance local.

Comprender el alcance es crucial para evitar errores y escribir código que funcione correctamente.

<br> 

## Diseño Modular: Dividiendo el Problema

La **modularidad** es la práctica de dividir un programa grande en partes más pequeñas, independientes y manejables (módulos o funciones). Cada módulo/función debe tener una responsabilidad clara.

En este módulo, tus funciones son tus "módulos". En lugar de tener todo el código en el `main`, divides las tareas en funciones: una función para leer datos, otra para calcular algo, otra para imprimir resultados, otra para validar, etc.

Esto no solo hace que tu código sea más organizado, sino que también te prepara para problemas del mundo real, donde los sistemas son complejos y necesitan ser divididos para ser manejados.

