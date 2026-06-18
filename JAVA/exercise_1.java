
import java.util.Scanner;
public class exercise_1 {
    public static void main(String[] args) {

        double length;
        double width;
        double area;

        Scanner input = new Scanner(System.in);

        System.out.println("Find the area of a Rectangle!");
        System.out.print("Enter Length: ");
        length = input.nextDouble();

        System.out.print("Enter width: ");
        width = input.nextDouble();

        area = length * width;

        System.out.printf("The Area is: %.2f cm^2", area);




        input.close();




    }
}
