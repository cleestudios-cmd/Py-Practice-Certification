import java.util.Scanner;

// -b +- sqrt b^2 - 4(ac) /2(a)

public class OUTPUT2_QUADRATIC {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        System.out.println("Enter the the Variable A");
        double a = scanner.nextDouble();
        System.out.println("Enter the the Variable B");
        double b = scanner.nextDouble();
        System.out.println("Enter the the Variable C");
        double c = scanner.nextDouble();

        double Phase_1 = -b;
        double Phase_2 = Math.pow(b, 2) - (4 * a * c);
        if (Phase_2 < 0) {
            System.out.println("No real solutions");
        }else {
            double Phase_3 = Math.sqrt(Phase_2);
            double Phase_4 = 2 * a;

            double Phase_5 = ((Phase_1 + Phase_3) / Phase_4);
            double Phase_6 = ((Phase_1 - Phase_3) / Phase_4);


            System.out.println(Phase_5);
            System.out.println(Phase_6);
        }



    }

}
