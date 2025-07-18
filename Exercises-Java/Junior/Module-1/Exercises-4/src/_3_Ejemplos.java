public class _3_Ejemplos {
    public static void modificarNumero(int numero){
        System.out.println("Dentro del metodo - antes de modificar" + numero);
        numero *= 2;
        System.out.println("Dentro del metodo - despues de modificar" + numero);
    }


    public static void main(String[] args) {
        int miNumero = 10;
        System.out.println("Antes de llamar al metodo: " + miNumero);

        modificarNumero(miNumero); // Paso por valor : copias 

        System.out.println("Despues de llamar al metodo: " + miNumero);
        /*Antes de llamar al metodo: 10
          Dentro del metodo - antes de modificar10
          Dentro del metodo - despues de modificar20
          Despues de llamar al metodo: 10 
          
          podria alterar el valor de la variable miNumero:
          miNumero = numero y con un return en vez del sout en la funcion modificarNumero*/

          System.out.println(esPar(23)); //se imprime si no tiene un sout dentro de la funcion, si no no da resultado alguno
    }


    public static boolean esPar(int numero) {
        var residuo = numero % 2;
        /*if (residuo == 0){
              return true; // --> boolean
              //Ahora el boolean es true y es lo que devuevle la funcion
          }else{
              return false;
          } */
         return residuo == 0;        
    }// toda funcion con algo diferente a void, debe devolver un return
    
}
