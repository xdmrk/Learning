public class _5_For {
    public static void main(String[] args) {

        for(int i = 0; i < 5; i++) { 
            /* 1.   int i = 0: inicializa una variable
             * 2.   i < 5: Valida si cumple la condicion
             * 3.   Imprime (ejecuta bloque{} de codigo)
             * 4.   i++: incrementa +1
             */
            System.out.println("Hola");
        }


        for(int i = 0; i < 5; i+=2) { //sumara de a dos 
            System.out.println("Hola");
        }


        for(int i = 1; i <= 3; i++) { //este for se ejecutara hasta que i = 3
            for(int j = 1; j <= 3; j++) {
                if (i == j)
                    break; // Salimos del bloque for j y regresamos al for i
                System.out.println(i + ", " + j + " ");
                // Salida: 2, 1 3, 1 3, 2

            }

        }
    }
    
}
