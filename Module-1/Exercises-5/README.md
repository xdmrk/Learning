# Estructuras Condicionales

Estructuras de control que permiten ejecutar diferentes bloques de código  _solo si_ una condición específica es verdadera (`true`).

**Características clave**:
* Evalúan expresiones booleanas (verdaderas o falsas)
* Se ejecutan una sola vez (a menos que estén dentro de un bucle)
* Deciden qué camino de ejecución seguir
* Ejemplos: `if`, `else if`, `else`, `switch`

**Propósito principal**: Tomar decisiones en el flujo del programa.

<!-- por arreglar. -->
### Expresiones Booleanas: La Base de las Decisiones

Una condición es una expresión que se evalúa a un valor booleano: `true` o `false`. Para construir condiciones, usamos:

- **Operadores de Comparación**: Comparan dos valores y devuelven `true` o `false`.

  | Operador | Descripción | Ejemplo | Resultado |
  | :-: | --- | :-: | :-: |
  | `==` | Igual a | `5 == 5` | `true` |
  | `!=` | Diferente de | `5 != 3` | `true` |
  | `>` | Mayor que | `7 > 3` | `true` |
  | `<` | Menor que | `2 < 5` | `true` |
  | `>=` | Mayor o igual que | `5 >= 5` | `true` |
  | `<=` | Menor o igual que | `3 <= 4` | `true` |

  ```Java
  int a = 10;
  int b = 5;
  boolean esIgual = (a == b); // false
  boolean esMayor = (a > b);  // true
  ```

- **Operadores Lógicos**: Combinan o modifican expresiones booleanas. Son esenciales para crear condiciones más complejas.

  - `&&` **(AND Lógico)**: El resultado es `true` si ambas condiciones son `true`. Si alguna es `false`, el resultado es `false`.

    | `Condición 1` | `Condición 2` | `Condición 1 && Condición 2` |
    | :-: | :-: | :-: |
    | true | true | true |
    | true | false | false |
    | false | true | false |
    | false | false | false |

    ```Java
    int edad = 20;
    double salario = 1500.0;

    // ¿Es mayor de 18 Y gana más de 1000?
    boolean cumpleRequisitos = (edad >= 18) && (salario > 1000); // true && true -> true
    ```

  - `||` **(OR Lógico)**: El resultado es `true` si al menos una de las condiciones es `true`. Solo es `false` si ambas condiciones son `false`.

    | `Condición 1` | `Condición 2` | `Condición 1 \|\| Condición 2` |
    | :-: | :-: | :-: |
    | true | true | true |
    | true | false | true |
    | false | true | true |
    | false | false | false |

    ```Java
    boolean tieneDescuento = false;
    boolean esClienteVIP = true;

    // ¿Tiene descuento O es cliente VIP?
    boolean aplicaBeneficio = tieneDescuento || esClienteVIP; // false || true -> true
    ```

  - `!` **(NOT Lógico)**: Invierte el valor booleano de una condición. Si la condición es `true`, `!condicion` es `false`, y viceversa.

    | `Condición` | `! Condición` |
    | :-: | :-: |
    | true | false |
    | false | true |

    ```Java
    boolean estaActivo = true;
    boolean estaInactivo = !estaActivo; // !(true) -> false
    ```

Combinando operadores de comparación y lógicos, puedes crear condiciones muy específicas:

```Java
int temperatura = 25;
boolean estaLloviendo = false;

// ¿La temperatura está entre 20 y 30 grados (inclusive) Y NO está lloviendo?
boolean climaAgradable = (temperatura >= 20 && temperatura <= 30) && !estaLloviendo;
// (true && true) && !(false) -> true && true -> true
```
<!-- por arreglar. hasta aqui -->
<br><!-- salto de linea forzados -->
<br>  
# Bucles (Ciclos)
Estructuras de control que permiten repetir la ejecución de un bloque de código múltiples veces mientras se cumpla una condición.

**Características clave**:
* Repiten la ejecución de código
* Tienen un mecanismo de control (contador, condición, etc.)
* Pueden ejecutarse desde 0 a N veces (o infinitamente si hay error)
* Ejemplos: `for`, `while`, `do-while`, `for-each`

**Propósito principal**: Automatizar repetición de tareas.
<!-- por arreglar. hasta aqui 
[Encabezados](#Diferencia-fundamental) enlaces
-->
<br>

### Diferencia fundamental
  | Característica	| Condicionales	| Bucles |
  | :-: | :-: | :-: |
  | Ejecución	| Una vez (por evaluación) |	Múltiples veces |
  |Propósito	| Tomar decisiones	| Repetir acciones |
  | Mecanismo	| Evalúa condición	| Controla repetición |
  | Ejemplos típicos	| if, switch	| for, while, do-while |
  

**Analogía**:
* Un **condicional** es como un cruce de caminos (elige un camino)
* Un **bucle** es como una calle circular (da vueltas hasta salir)
