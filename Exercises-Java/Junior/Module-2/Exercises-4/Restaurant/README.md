# Modelando un Sistema Básico de Restaurante

**Reglas de Codificación**: Escribe el código en **inglés**. Los comentarios dentro del código y los mensajes de salida en consola (`System.out.println`, `printf`) deben estar en **español**.

### Identificar las Entidades Principales

Discutir qué "cosas" o conceptos son importantes en un sistema de restaurante (Restaurante, Mesa, Pedido, Ítem del Menú, Ítem del Pedido, Empleado/Mesero).

## Clase `Restaurant`

- **Atributos privados**: `name` (String), `address` (String).
- **Relación con Mesas (Agregación)**: Añade un atributo `private Table[] tables;`. El restaurante _agrega_ mesas que existen independientemente. Pasa un Array de objetos `Table` al constructor del `Restaurant`.
- **Relación con Empleados (Agregación)**: Añade un atributo `private Employee[] employees;`. Pasa un Array de objetos `Employee` al constructor.
- **Relación con Menú (Composición o Agregación)**: Crea una clase `Menu`. Decide si el `Menu` _compone_ el `Restaurant` o es _agregado_. Implementa la relación con un atributo `private Menu menu;`. Si es composición, crea el `Menu` dentro del constructor del `Restaurant`. Si es agregación, pásalo al constructor.
- Constructor que inicialice los atributos y reciba los Arrays de `Table` y `Employee` y el objeto `Menu`.
- Getters para todos los atributos.
- Método `displayMenu()`: Llama al método `displayItems()` del objeto `Menu`.
- Método `findTable(int tableNumber)`: Recorre el array `tables` y retorna la `Table` con el número especificado, o `null` si no se encuentra.

## Clase `Table`

- **Atributos privados**: `tableNumber` (int), `capacity` (int), `isOccupied` (boolean - inicialmente false).
- **Relación con Pedido (Asociación)**: Añade un atributo `private Order currentOrder;`. Una mesa _tiene un_ pedido actual. Implementa la relación.
- Constructor.
- Getters.
- Setter para `isOccupied`.
- Método `assignOrder(Order order)`: Asigna un `Order` a `currentOrder` y setea `isOccupied` a `true`.
- Método `clearTable()`: Setea `isOccupied` a `false` y `currentOrder` a `null`.
- Método `getCurrentOrder()`: Retorna el `currentOrder`.

## Clase `MenuItem`

- **Atributos privados**: `name` (String), `price` (double).
- Constructor.
- Getters.

## Clase `OrderItem`

- **Atributos privados**: `menuItem` (una referencia a un objeto `MenuItem`), `quantity` (int).
- Constructor que reciba un `MenuItem` y una `quantity`.
- Getters.
- Método `calculateSubtotal()` que retorne el precio del `MenuItem` por la `quantity`.

## Clase `Order`

- **Atributos privados**: `orderNumber` (int), `status` (String - ej. "Pending", "In Progress", "Delivered").
- `Relación con Ítems del Pedido (Composición)`: Añade un atributo `private OrderItem[] items;`. El pedido _compone_ ítems. El Array `items` debe ser **creado dentro del constructor** de `Order`, recibiendo el tamaño máximo de ítems.
- Constructor que inicialice el número y estado, y cree el array `items` con un tamaño dado.
- Método `addItem(OrderItem item)`: Añade un `OrderItem` al array `items` en la primera posición `null` disponible. Debe manejar el caso de que el array esté lleno.
- Getters.
- Método `calculateTotal()`: Itera sobre el array `items`, suma el subtotal de cada `OrderItem` (verificando que no sea `null`) y retorna el total.
- Método `displayDetails()`: Imprime el número del pedido, estado y los detalles de cada ítem en el array `items`.

## Clase `Menu`

- **Atributos privados**: name (String).
- **Relación con Ítems del Menú (Agregación)**: Añade un atributo `private MenuItem[] items;`. El menú _agrega_ ítems. El Array `items` debe ser **pasado al constructor** de `Menu`.
- Constructor que inicialice el nombre y reciba un Array de `MenuItem`s.
- Getters.
- Método `displayItems()`: Itera sobre el array `items` e imprime los detalles de cada `MenuItem`.
- Método `findItem(String itemName)`: Recorre el array `items` y retorna el `MenuItem` con el nombre especificado, o `null` si no se encuentra.

## Clase `Employee`

- **Atributos privados**: `name` (String).
- Constructor.
- Getter.

## Clase Principal (`main`)

- Crea una clase principal (ej. `RestaurantApp.java`) con un método `main`.
- Dentro de `main`:
  - Crea algunos objetos `MenuItem`.
  - Crea un Array de `MenuItem`s y úsalo para crear un objeto `Menu`.
  - Crea un Array de objetos `Table` y úsalo para crear un objeto `Restaurant`.
  - Crea un Array de objetos `Employee` y úsalo para crear el mismo objeto `Restaurant`.
  - Llama a `restaurant.displayMenu()`.
  - Crea un objeto `Order`, especificando un tamaño máximo de ítems (ej. 5).
  - Busca `MenuItem`s en el `Menu` (usando `menu.findItem()`) y úsalos para crear objetos `OrderItem`.
  - Añade los `OrderItem`s al `Order` (usando `order.addItem()`).
  - Busca una `Table` en el `Restaurant` (usando `restaurant.findTable()`) y asigna el `Order` a esa `Table`.
  - Llama a `order.displayDetails()` y `order.calculateTotal()`.
  - Demuestra la relación bidireccional si la implementaste (ej. desde el pedido, acceder a la mesa si es posible).
