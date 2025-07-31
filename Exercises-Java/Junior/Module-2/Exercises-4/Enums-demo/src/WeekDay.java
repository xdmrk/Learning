public enum WeekDay { // una clase tipo enumns

    // Constantes
    MONDAY(1, "Lunes"), TUESDAY(2, "Martes"), WEDNESDAY(3, "Miercoles"), THURSDAY(4, "Jueves"), FRIDAY(5, "Viernes"),
    SATURDAY(6, "Sabado"), SUNDAY(7, "Domingo"); // (Datos del constructor)

    private Integer num;
    private String name;

    // Constructor
    WeekDay(Integer num, String name) {
        this.name = name;
        this.num = num;
    }

    public Integer getNum() {
        return num;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() { // Imprimira Lunes
        return getName();
    }

}
