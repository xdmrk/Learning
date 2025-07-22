public class Dog extends Animal { // Dog sale inicialmente con error porque no existe en la clase animal un
                                  // constructor vacio
    private String breed;

    public Dog(String name, Integer age, String breed) {
        super(name, age); // esta debe ser la primera linea de este constructor debe ser llamar al
                          // constructor de clasePadre a menos que esta tenga un constructor vacio
        this.breed = breed;
    }

    public String getBreed() {
        return breed;
    }

    public void eat(String food) {
        // System.out.println(name + " come " + food); error: name es un atributo
        // privado de clasePadre
        System.out.println(getName() + " come " + food);
    }

    public void bark() {
        makeNoise(); // Utiliza el makeNoise()sobrescrito de clase Dog, si no tuviera utilizaria el
                     // de clase Animal
    }

    @Override
    public void makeNoise() {
        System.out.println("Gua Gua Gua");
    }

}
