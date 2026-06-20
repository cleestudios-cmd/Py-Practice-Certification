import java.util.Scanner;


public class OUTPUT1_COLLATZ {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        while (true) {

            System.out.print("\nEnter a Number: ");
            int n = scanner.nextInt();

            if (n <= 0) {
                System.out.println("Invalid Input");
                continue;
            }
            if (n == 1) {
                System.out.println("Sequence Ends; Total Steps: 0");
                continue;
            }
            int steps = 0;
            while (true) {

                if (n % 2 == 0) {
                    System.out.printf("%d is Even --> %d/2\n", n, n);
                    n = n / 2;
                    steps++;
                    if (n == 1) {
                        System.out.printf("Sequence Ends; Total Steps: %d", steps);
                        break;
                    }
                    
                }
                else if (n % 2 == 1) {
                    System.out.printf("%d is Odd --> 3(%d) + 1\n", n, n);
                    n = 3 * n + 1;
                    steps++;
                    if (n == 1) {
                        System.out.printf("Sequence Ends; Total Steps: %d", steps);
                        break;
                    }
                    
                }



            }
        }
    }
}