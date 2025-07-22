public class Animal {
    //ATRIBUTOS
    private String name;
    private Integer age;    

    //CONSTRUCTOR
    public Animal(String name, Integer age) {
        this.name = name;
        this.age = age;
    }


    public String getName() { //Obtener nombre
        return name;
    }

    public Integer getAge() {
        return age;
    }    

    //METODOS
    public void sleep(){
        System.out.println("Zzz z  z   z");
    }

    public void makeNoise(){
        System.out.println("Grrrr");
    }


    

}
