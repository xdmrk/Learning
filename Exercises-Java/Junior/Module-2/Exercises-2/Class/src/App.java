public class App {
    public static void main(String[] args) {
        animalSample();
    }

    private static void animalSample() {
        Animal animal1 = new Dog("Buddy", 3, "labrador");        
        System.out.println("Nombre: " + animal1.getName());
        animal1.makeNoise(); // Esta llamando la implementacion de la clase Dog porque estamos creando un
                             // objeto new Dog y porque tiene sobreescritura
        ((Dog) animal1).eat("Concentrado"); // Casting: animal1 tipo Animal quiero convertirla en una claseHijo (NO
                                            // RECOMENDADO)
        ((Dog) animal1).bark();
        animal1.sleep();
        // Nombre: Buddy
        // Gua Gua Gua
        // Buddy come Concentrado
        // Gua Gua Gua
        // Zzz z z z

        Dog animal2 = new Dog("Buddy", 3, "labrador");
        System.out.println("Nombre: " + animal2.getName());
        animal2.makeNoise();
        animal2.eat("Concentrado");
        animal2.bark();
        animal2.sleep();
        // Nombre: Buddy
        // Gua Gua Gua
        // Buddy come Concentrado
        // Gua Gua Gua
        // Zzz z z z

        Animal animal3 = new Cat("Sushi", 2);
        System.out.println("Nombre: " + animal3.getName());
        animal3.makeNoise();
        // ((Dog) animal3).eat("Concentrado"); ERROR: clase Cat no tiene relacion alguna
        // con clase Dog
        ((Cat)animal3).scratch();
        animal3.sleep();
    }
}
