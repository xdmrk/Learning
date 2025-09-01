# Conceptos del lenguaje

## Manejo de errores y excepciones en Java
Los términos error y excepción se utilizan para manejar problemas que ocurren durante la ejecución de un programa, pero tienen significados y usos diferentes.

![Throwable](resources\Throwable.png)

### ¿Qué entendemos como errores?
Son **problemas graves** que generalmente indican que la JVM (Java Virtual Machine) **no puede continuar ejecutando el programa**. Estos problemas suelen ser externos al control del programa y es poco probable que se puedan recuperar de ellos.

#### Características principales
- No se espera que sean manejados o capturados.
- Son condiciones críticas, como problemas de memoria (`OutOfMemoryError`), fallos en el hardware, errores de inicialización del sistema, entre otros.
- Derivan de la clase `Error`, que es una subclase de `Throwable`.

### ¿Qué entendemos como excepciones?
Son **condiciones anómalas** que ocurren durante la ejecución de un programa y que un programa **puede manejar** y de las cuales **puede recuperarse**.

#### Características principales:
- Se espera que se manejen usando bloques `try-catch`.
- Pueden ser **verificadas** (checked) o **no verificadas** (unchecked).
- Derivan de la clase `Exception`, que también es una subclase de `Throwable`.

![Jerarquia de Excepciones](https://cdn.javarush.com/images/article/f23906db-7512-4047-985d-8ddb6bbc99c9/1024.webp)

#### Excepciones Verificadas (_Checked_)
- Son excepciones que deben ser declaradas en el método que las puede lanzar o deben ser capturadas.
- Ejemplo: `IOException`, `SQLException`.

#### Excepciones No Verificadas (_Unchecked_)
- Son excepciones que no requieren ser declaradas ni capturadas obligatoriamente.
- Ejemplo: `NullPointerException`, `ArrayIndexOutOfBoundsException`.

![Tipos de excepciones](https://cdn.javarush.com/images/article/2e4a84d4-3d29-41a2-b6f9-32ae87e9ee96/1024.webp)

### Por que es importante el manejo de excepciones en el desarrollo profesional
- Al manejar excepciones, los desarrolladores pueden crear aplicaciones más robustas que no se bloqueen ante eventos inesperados.
- Facilita el mantenimiento del código, ya que permite identificar y manejar errores de manera organizada.
- Ayuda a prevenir problemas de seguridad al manejar adecuadamente las excepciones y evitar que se propaguen.
- Mejorar la experiencia del usuario al proporcionar mensajes de error claros y evitar bloqueos inesperados.

´´´java
public static void main(String arg[]) {
    int [] array = new int[20];
    array[-3] = 24;
}
´´´

