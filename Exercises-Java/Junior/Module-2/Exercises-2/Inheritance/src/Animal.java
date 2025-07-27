public abstract class Animal { // abstract: no se pueden crear objetos a partir de esta clase ya que
                               // estapensada como una generalización
    private String name;
    private Integer age;
    private String genre;

    public Animal(String name, Integer age, String genre) {
        this.name = name;
        this.age = age;
        this.genre = genre;
    }

    public String getName() {
        return name;
    }

    public Integer getAge() {
        return age;
    }

    public String getGenre() {
        return genre;
    }

    protected void setName(String name) {
        this.name = name;
    }

    public abstract void hunt();

    public abstract void makeNoise();

    public void happyBirthday() {
        age++;
    }

}
