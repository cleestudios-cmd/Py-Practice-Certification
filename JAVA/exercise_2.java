import java.util.Scanner;

public class exercise_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] fruit = {"Apple", "Banana", "Mango"};
        int apple = 10;
        int banana = 15;
        int mango = 20;
        System.out.print("Pick a fruit to buy: ");
        String item = scanner.nextLine();
        if (item.equals(fruit[0])) {
            System.out.print("Apple is $10, Buy? ");
            String second = scanner.nextLine();
            if (second.equals("Yes")) {
                System.out.print("Enter Payment: $");
                int cash = scanner.nextInt();
                int total = cash - apple;
                if (total == 0) {
                    System.out.print("Thank You for Your Purchase!");
                } else {
                    System.out.printf("Your change is $%d", total);
                }
            }
        }
        if (item.equals(fruit[1])) {
            System.out.print("Banana is $15, Buy? ");
            String second = scanner.nextLine();
            if (second.equals("Yes")) {
                System.out.print("Enter Payment: $");
                int cash = scanner.nextInt();
                int total = cash - banana;
                if (total == 0) {
                    System.out.print("Thank You for Your Purchase!");
                } else {
                    System.out.printf("Your change is $%d", total);
                }
            }
        }
        if (item.equals(fruit[2])) {
            System.out.print("Mango is $20, Buy? ");
            String second = scanner.nextLine();
            if (second.equals("Yes")) {
                System.out.print("Enter Payment: $");
                int cash = scanner.nextInt();
                    int total = cash - mango;
                    if (total == 0) {
                        System.out.print("Thank You for Your Purchase!");
                    } else {
                        System.out.printf("Your change is $%d", total);
                    }
                }
            }


            scanner.close();


        }
    }

