public class Fish extends Animal implements CanSwim {
    private String color;
    private Boolean formSea;

    public Fish(String name, Integer age, String genre, String color, Boolean formSea) {
        super(name, age, genre);
        this.color = color;
        this.formSea = formSea;
    }

    public String getColor() {
        return color;
    }

    public Boolean getFormSea() {
        return formSea;
    }

    @Override // -> Lo pongo a ser por implementación
    public void swin() {
        System.out.printf("%s esta nadando%n", getName());
    }

    public boolean canPutEggs() {
        return getGenre().equalsIgnoreCase("hembra");
    }

    @Override
    public void hunt() {        
        System.out.printf("%s esta nadando, abre la boca y se lanza a por él%n", getName());
    }

    @Override
    public void makeNoise() {
        System.out.printf("%s hace Glob Glob%n", getName());
    }
}
