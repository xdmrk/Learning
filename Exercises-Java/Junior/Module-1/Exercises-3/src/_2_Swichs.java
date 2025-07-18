public class _2_Swichs {
    public static void main(String[] args) {
        
        int dia = 1;
        switch(dia){ // Expresión Switch
            case 1: System.out.println("Lunes"); break;
            case 2: System.out.println("Martes"); break;
            case 3: System.out.println("Miercoles"); break;
            case 4: System.out.println("Jueves"); break;
            case 5: System.out.println("Viernes"); break;
            case 6: System.out.println("Sabado"); break;
            case 7: System.out.println("Domingo"); break;
        }


        char letra = 'A'; //No solo evalua condiciones, tambien valores
        switch (letra){ 
            case 'A': System.out.println("Vocal A"); break;    
            case 'B': System.out.println("Vocal B"); break;    
            default: System.out.println("Otra letra");
        } 


        String fruta = "Manzana";
        switch (fruta){ 
            case "Manzana": System.out.println("La fruta es manzana"); break;    
            case "Pera": System.out.println("La fruta es pera"); break;    
            default: System.out.println("Otra fruta");
        } 


        int dias = 1;
        String nombre = switch(dias){ // Expresión Switch (Java 14+)
            case 1 -> "Lunes";
            case 2 -> "Martes";
            default -> "Otro";
        };System.out.println(nombre);


        int n = 5;
        String res = switch(n){
            case 5 -> {
                yield "Cinco"; // yiels: asigna valor a res
            }
            default -> "Otro";
        };System.out.println(res);
    }
    
}
