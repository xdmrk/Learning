public class App {
    public static void main(String[] args) throws Exception //Firma del metodo
    {
        // //cuepo de la funcion { }
        // SumarNu(10, 5); //(10, 5): Argumentos

        Perro miMascota = new Perro(); //aqui estoy usando ña clase
        //miMascota: instancia
        miMascota.ladrar(); //App es cliente de la clase Perro


        Calculadora calculadora = new Calculadora();
        int miSuma = calculadora.Sumar(1, 9, 11);
        Pantalla pantalla = new Pantalla();
        pantalla.mostrar(miSuma);

        int miResta = calculadora.Restar(9,5);
        pantalla.mostrar(miResta);

    }
}


        
