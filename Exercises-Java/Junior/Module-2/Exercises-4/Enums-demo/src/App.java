public class App {
    public static void main(String[] args) {
        WeekDay day = null; // null: sin asignar
        day = WeekDay.MONDAY;
        System.out.println(day); //Llama al metodo toString por lo que sin definirlo seguiria imprimiendo MONDAY
        System.out.println(day.getNum());

        var appointmentDay = WeekDay.FRIDAY;
        System.out.println(appointmentDay);
    }
}
