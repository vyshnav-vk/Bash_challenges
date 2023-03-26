import java.util.Scanner;
public class graduate extends student {
    
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter research area:");
    String researchArea = scanner.nextLine();

    graduate p = new graduate();
    p.printInfo(b+"Research Area: " + researchArea);
    
    

}