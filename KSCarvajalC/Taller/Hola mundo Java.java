import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("N: ");
        int n = input.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("hola mundo.");
        }
    }
}
