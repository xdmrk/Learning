public class Duck extends Animal implements CanFly, CanRun, CanSwim{ //Bombillo: Add unimplemented methods, implementa los metodos abstractos de la clasePadre
    private String color; //Bombillo: Add uniplemented methods, implementa los metodos abstractos de clasePadre

    public Duck(String name, Integer age, String genre, String color) {
        super(name, age, genre);
        this.color = color;
    }

    public String getColor() {
        return color;
    }
    
    @Override // -> Lo pongo a ser por implementación
    public void swin() {
        System.out.printf("%s esta nadando%n", getName());
    }
    
    @Override // -> Lo pongo a ser por implementación
    public void fly() {
        System.out.printf("%s esta volando%n", getName());
    }

    @Override // -> Lo pongo a ser por implementación
    public void run() {
        System.out.printf("%s esta corriendo%n", getName());
    }

    public boolean canPutEggs() {
        return getGenre().equalsIgnoreCase("hembra");
    }

    @Override
    public void hunt() {
        System.out.printf("%s va nadando, se posa sobre el pez y mete la cabeza para cazarlo%n", getName());
    }

    @Override
    public void makeNoise() {
        System.out.printf("%s hace Cuak Cuak%n", getName());
    }

    

}
