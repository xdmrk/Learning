package model;

import java.time.LocalDate;

public class History {
    private String description;
    private LocalDate date;
    private User user;

    
    public History(String description, User user) {
        this.description = description;
        this.date = LocalDate.now();
        this.user = user;
    }

    public String getDescription() {
        return description;
    }

    public LocalDate getDate() {
        return date;
    }

    public User getUser() {
        return user;
    }

}
