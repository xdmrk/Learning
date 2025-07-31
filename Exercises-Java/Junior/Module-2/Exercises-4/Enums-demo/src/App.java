public class App {
    public static void main(String[] args) {
        WeekDay day = null; // null: sin asignar
        day = WeekDay.MONDAY;
        System.out.println(day); //Llama al metodo ToString por lo que sin definirlo seguiria imprimiendo MONDAY
    }
}
