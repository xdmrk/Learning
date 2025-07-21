import java.time.LocalDate;

public class App {
    public static void main(String[] args) {
        Book book1 = new Book(); // -> inicializar llamando el constructor // Book o var si tenemos el
                                 // constructor inicializado
        var book2 = new Book("Programacion", "pedro", 900);
        var book3 = new Book("Learning english", "Duran", 200, LocalDate.of(2010, 10, 21), "English school",
                "Aprendizaje");

        System.out.println(book1.toString());
        System.out.println(book2.giveMeYourTitle());
        System.out.println(book3.toString());

        var person1 = new Persona("Astro", "Toronto");

        System.out.println(person1.toString());

    }

}
