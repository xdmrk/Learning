public class Calculadora {

    //Atributos
    int resultado;


    public int Sumar(int a, int b, int resultado) {
        resultado = this.resultado;
        this.resultado = a + b;
        return this.resultado;// -->Resultado del metodo
    }

    public int Restar(int a, int b) {
        resultado = a - b;
        return resultado;
    }

}
