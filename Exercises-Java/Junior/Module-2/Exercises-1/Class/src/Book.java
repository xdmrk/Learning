import java.time.LocalDate;

public class Book { // New Java File >> Class
    // Atributos
    // Wrapper Classes: Integer, Character, Long, Byte, Short, Float, Double,
    // Boolean
    private String title;
    private String author; // private: otras clases no podran manipular estos atributos
    private Integer pages; // Integer --> int (envuelve a int)
    private LocalDate publishDate; // Una clase del paquete java.time
    private String editor;
    private String category;
    // estas variables Integer, etc no tienen datos (null)

    // Constructor -> inicializar el objeto
    // Autoboxing: int -> Integer
    // Unboxing: Integer -> int
    public Book() {
        // Constructor por defecto, si no se escribe java lo crea por defecto, sin
        // parametros
        title = "Las aventuras";
        author = "Arturitu";
        pages = 100;
        publishDate = LocalDate.now();
        editor = "Pergamino";
        category = "Aventure";
    }

    public Book(String title, String author, Integer pages) {
        // Como tenemos los mismos nombres de variables necesitamos el this para
        // identificar
        this.title = title;
        this.author = author; // This. >> variable local de clase
        this.pages = pages;
        publishDate = LocalDate.now();
        editor = "Pergamino";
        category = "Aventure";
    }

    public Book(String title, String author, Integer pages, LocalDate publishDate, String editor, String category) {
        this.title = title;
        this.author = author;
        this.pages = pages;
        this.publishDate = publishDate;
        this.editor = editor;
        this.category = category;
    }

    // Metodos -> acciones que quiero que haga la clase
    public String giveMeYourTitle() { // public -> cualquier otro objeto va a poder llamar a este metodo
        return title;
    }

    // Metodo getter -> Obtener los valores de los atributos
    public String getTitle() { // buena practica, llamar get a los metodos para obtener
        return title;
    }

    public String getAuthor() {
        return author;
    }

    // clic derecho > source action > Generate getters
    public Integer getPages() {
        return pages;
    }

    public LocalDate getPublishDate() {
        return publishDate;
    }

    public String getEditor() {
        return editor;
    }

    public String getCategory() {
        return category;
    }

    // Metodo Setter -> Cambiar de manera directa el valor de un atributo ->
    // set<atributo>(TipoDatos parametro)
    // set. -> te crea el setter segun atributo
    public void setCategory(String category) {
        this.category = category;
    }

    public String toString() {
        // toString(): clase por defecto (Book@jks8sddgy)
        return String.format(
                "Libro: titulo=%s, autor=%s, paginas=%s, publicacion=%s, editorial=%s, categoria=%s, getclass=%s",
                getTitle(), getAuthor(),
                getPages().toString(), getPublishDate().toString(), // ->Porque PublishDate es un objeto igual que
                                                                    // getPages con Integer
                getEditor(), getCategory(), getClass());
        // return "Libro [titulo: "+title+", autor: "+author+", paginas: "+pages+",
        // fecha"+publishDate+"]";
    }

}
