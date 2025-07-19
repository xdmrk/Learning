# SINTAXIS BÁSICA DE JAVA (CHEAT SHEET)

```java
  package team.xd; //Todos los archivos pertenecen a un paquete
  
  import java.lang.*; //Importa los paquetes para el proyecto
  
  public class Person { //Java usa clases para ejecutar el codigo
  
  private String name; //Se debe indicar el tipo de dato
  
  // public -> Modificadores de acceso: private, public, protected o por defecto ninguno
  //El metodo principal en Java es el metodo main
  public static void main(String args[]){
  
    //La palabra reservada new crea un objeto del tipo de dato especificado
    Person friend = new Person(); 
    friend.name = "Peter";
    System.out.println("Hola " + friend.name); //; se utiliza para cada sentencia

    } // Se usan llaves para identificar el bloque del codigo
  }
  ```

**Reglas Importantes**
- Todo debe estar dentro de una clase
- Cada sentencia termina con `;`
- Bloques de código se delimitan con `{}`
- Java es case-sensitive (Nombre ≠ nombre)
- El método main() es obligatorio para ejecución
- Usar // para comentarios de línea y /* */ para multilínea (`Ctrl K + C`: Comentar varias lineas)

## Estructura Mínima
```java
package mi.paquete;  // Obligatorio (por convención)
import java.util.*;   // Importar librerías

public class ClasePrincipal {  // Nombre = NombreArchivo.java
    public static void main(String[] args) {  // Punto de entrada
        System.out.println("Hola Mundo");  // Impresión
    }
}
```

## Estructura Fundamental
```java
package team.ed.course;       // Declaración del paquete (obligatorio)
import java.lang.*;           // Importación de librerías

public class Person {         // Clase principal (nombre en mayúscula)
    private String name;      // Atributo privado

    // Método principal (punto de entrada)
    public static void main(String args[]) {
        Person friend = new Person();  // Creación de objeto
        friend.name = "Peter";       // Asignación de atributo
        System.out.println("Hola " + friend.name);  // Salida por consola
    }
}
```

## Conceptos Clave
1. **Paquetes**:
   - Todos los archivos pertenecen a un paquete
   - Se declara con `package nombre.paquete;`
   - Convención: usar dominio inverso (ej: com.empresa.proyecto)

2. **Imports**:
   - Para usar clases de otros paquetes
   - java.lang.* se importa automáticamente

3. **Clases**:
   - Java es orientado a objetos (todo dentro de clases)
   - Nombre en PascalCase (Ej: `MiClase`)
   - Nombre del archivo = Nombre de la clase + `.java`

4. **Modificadores de Acceso**:
   - **`public`**: accesible desde cualquier clase
   - **`private`**: solo accesible dentro de su clase
   - **`protected`**: accesible en mismo paquete y subclases
   - **(default)**: solo accesible en mismo paquete

5. **Método main()**:
   - Punto de entrada del programa
   - Firma obligatoria: `public static void main(String[] args)`

6. **Creación de Objetos**:
   - Usando new: Person objeto = new Person();
   - La palabra reservada new asigna memoria
  
7. **Sintaxis Básica**:
   - Punto y coma (`;`) al final de cada sentencia
   - Llaves `{}` para delimitar bloques de código
   - Identación para mejor legibilidad (no obligatoria pero recomendada)


```java
package team.ed.course;

import java.util.Scanner;  // Importación específica

public class Person {
    // Atributos
    private String name;
    private int age;
    
    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // Método
    public void greet() {
        System.out.println("Hola, soy " + name + " y tengo " + age + " años.");
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese nombre: ");
        String nombre = sc.nextLine();
        
        Person person = new Person(nombre, 25);
        person.greet();
    }
}

```
  
