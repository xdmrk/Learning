public class _1_Funcion {
    public static void main(String[] args) {
        System.out.println(esPar(11)); //--> False
        // ctrl sostenido + "esPar" lleva a la funcion
        // en main se ejecuta 

        saludar();

    }

    public static void exampleOne() {// funcion
        //public, statid: modificadores    |   void: tipo de dato  |   (parametros)
        //Static: no necesitamos crear un objeto para poder llamar la funcion
        //void: tipo de dato que espero que me devuelva la funcion
        //void: no retorna ningun valor para guardar en alguna variable
        //nombre de la funcion en camelCase (holaMundoHi)

        //bloque de codigo de la funcion ejercicio5
    }


    public static boolean esPar(int numero) {
        var residuo = numero % 2;
        if (residuo == 0){
            return true; // --> boolean
            //Ahora el boolean es true y es lo que devuevle la funcion
        }else{
            return false;
        }
    }


    public static void saludar() {
        System.out.println("Buen dia");
    }




}
