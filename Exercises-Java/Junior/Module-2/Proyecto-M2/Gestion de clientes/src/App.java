import app.View;
import model.GestionUsers;
import model.Rol;
import model.User;

public class App {
    public static void main(String[] args) throws Exception {        
        usersSample();
        View menu = new View();
        menu.menudeInicio();

        
        
        
    }

    private static void usersSample() {
        GestionUsers.DEFAULT_USERS[0] = new User("astro","de las estrellas", "xdmrk", "1234567");
        GestionUsers.DEFAULT_USERS[1] = new User("maria", "Nieto", "mari72637", "cuchurrumi", Rol.ADMIN);
    

        }
    }
