public class Perro {
    //src/ New java file/ class

    String nombre;
    int edad;

    //CONSTRUCTOR(ES)
    public Perro(String nombre){
        this.nombre = nombre;
    }
    

    public Perro(){
    }


    public Perro(String nombre, int edad){
        this.nombre = nombre;
        this.edad = edad;
    }
    //Sobrecarga - tenemos tres constructores llamados igual
    //cambia la firma










    public void ladrar(){
        System.out.println("dice: Guau!");
    }

}
