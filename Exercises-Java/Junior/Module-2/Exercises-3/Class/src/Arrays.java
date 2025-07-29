import java.util.Scanner;

public class Arrays {
    public static void main(String[] args) {

        //ARRAYS
        int[][] board = new int[3][]; // El primer array tendra 3 posiciones, el segundo sera dinamico
        board[0] = new int[3]; // El indice 0 (primer elemento) tendra 3 elementos
        board[0][0] = 1;
        board[0][1] = 2;
        board[0][2] = 3;

        board[1] = new int[6];
        board[1][0] = 4;
        board[1][1] = 5;
        board[1][2] = 6;
        board[1][3] = 7;
        board[1][4] = 8;
        board[1][5] = 9;

        board[2] = new int[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }; // Array de tamaño dinamico

        //IMPRESION 
        System.out.println();
        System.out.println(board.length); // Cantidad de elementos del primer Array [3][]

        for (int i = 0; i < board.length; i++) {
            System.out.println(board[i].length + " "); // Cantidad de elementos de cada indice del primer array (3, 6, 10)
        }
        System.out.println();

        for (int row = 0; row < board.length; row++) { // Fila
            for (int column = 0; column < board[row].length; column++) { // Columna
                System.out.print(board[row][column] + " "); // Elementos de cada array 
            } 
            System.out.println();
        }


        //ARRAYS CON SCANNER
        System.out.println();
        var sc = new Scanner(System.in);

        System.out.print("Ingrese el numero de filas: ");
        var tamaño = sc.nextInt(); //Numero de filas
        int[][] boardQuestion = new int[tamaño][]; //Se define la primera dimension (filas)

        for (int row = 0; row < boardQuestion.length; row++) { // Recorriendo cada fila del array
            System.out.printf("Ingrese el numero de columnas de la fila %d: ", (row + 1));
            tamaño = sc.nextInt();
            boardQuestion[row] = new int[tamaño]; //Se define el tamaño del array para la segunda dimension (columnas)    
            
            for (int column = 0; column < boardQuestion[row].length; column++) { //Recorriendo cada columna de la fila del tablero
                System.out.printf("Ingrese el valor para la fila %d, %d: ", (row + 1), (column + 1));   
                boardQuestion[row][column] = sc.nextInt();             
            }
        }
        sc.close();


        System.out.println();

        //IMPRESION DEL ARRAY SOLICITADO
        System.out.println("==== Contenido del tablero ====");
        for (int row = 0; row < boardQuestion.length; row++) { // Fila
            for (int column = 0; column < boardQuestion[row].length; column++) { // Columna
                System.out.print(boardQuestion[row][column] + " "); // Elementos de cada array 
            } 
            System.out.println();
        }
    }
}
