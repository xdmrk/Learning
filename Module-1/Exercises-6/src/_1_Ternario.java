public class _1_Ternario {
    public static void main(String[] args){
        int numero = 0;

        // Operadores ternarios anidados
        String resultado = (numero == 0) ? "Cero" 
        : (numero % 2 == 0) ? "Par" // Si no se cumple la condicion, salta a validar la siguiente
        : "impar";
        
        System.out.println(resultado);
    }
}
