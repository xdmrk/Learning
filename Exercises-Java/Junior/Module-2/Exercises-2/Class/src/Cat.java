public class Cat extends Animal {

    public Cat(String name, Integer age) {
        super(name, age); 
    }

    public void scratch(){
        System.out.println("Lo dañe");
    }

    @Override
    public void makeNoise() {
        System.out.println("Miawwwwwwww");
    }
}
