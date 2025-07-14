public class _2_ParametrosArgumentos {
    public static void main(String[] args) {
        saludarNombre("Ana"); //"Ana" es el argumento para el parametro 'nombre'
        saludarNombre("Maria");
        
        imprimiRepetido("Repetir esto", 3); //"Repetir esto" y 3: los dos son argumentos
        //(String mensaje, int veces) deben tener el mismo orden
    }


    public static void saludarNombre(String nombre) {
        System.out.println("Hola " + nombre + "!");
        }
        
    
    public static void imprimiRepetido(String mensaje, int veces) {
        // Metodo con dos parametros: String y un int
        for (int i = 0; i <  veces; i++){
            System.out.println(mensaje);
        }   
    }
    
}
