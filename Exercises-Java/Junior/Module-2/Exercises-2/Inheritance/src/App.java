public class App {
    public static void main(String[] args) {
        var eagle = new Eagle("Gruño", 2, "hembra", "Arpia");
        var lion = new Lion("Scar", 4, "Macho", "Amarillo");
        var fish = new Fish("Nemo", 3, "Hembra", "Blanco", true);
        var duck = new Duck("Lucas", 5, "macho", "negro");
        System.out.println("\n");

        eagle.fly();
        eagle.hunt();
        eagle.happyBirthday();
        System.out.println("El aguila tiene " + eagle.getAge() + " años");
        System.out.println("El " + eagle.getName() + " " + (eagle.canPutEggs() ? "si" : "no") + " puede poner huevos");
        System.out.println("\n");

        lion.run();
        lion.hunt();
        lion.happyBirthday();
        System.out.println("El leon tiene " + lion.getAge() + " años");
        System.out.println("\n");

        fish.swin();
        fish.hunt();
        fish.happyBirthday();
        System.out.println("El pez tiene " + fish.getAge() + " años");
        System.out.println("El " + fish.getName() + " " + (fish.canPutEggs() ? "si" : "no") + " puede poner huevos");
        System.out.println("El " + fish.getName() + " " + (fish.getFormSea() ? "es de mar" : "es de rio"));
        System.out.println("\n");

        duck.swin();
        duck.fly();
        duck.run();
        duck.hunt();
        duck.happyBirthday();
        System.out.println("El pato tiene " + duck.getAge() + " años");
        System.out.println("El " + duck.getName() + " " + (duck.canPutEggs() ? "si" : "no") + " puede poner huevos");
        
        CanSwim animal1 = new Fish("Pato", 2, "hembra", "amarillo", false);
        animal1.swin();

        CanSwim animal2 = new Duck("Rogelio", 2, "macho", "blanco");
        animal2.swin();
        //Casting
        CanFly animal3 = (CanFly) animal2; 
        animal3.fly();
        Animal animal4 = (Animal) animal3;
        animal4.happyBirthday();
        animal4.makeNoise();



    }
}
