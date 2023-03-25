import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
public class student{
    public student(String name, int id) {
    }

    public static void main(String[] args){
        List<String> students = new ArrayList<>();
        while(true){
            try (Scanner scanner = new Scanner(System.in)) {
                System.out.println("Enter student name:");
                String name = scanner.nextLine();
                
                System.out.println("Enter student ID:");
                String id = scanner.nextLine();
                
                System.out.println("Enter student courses (separated by commas):");
                String courses = scanner.nextLine();
         
                List<String> course = new ArrayList<>();
                course.add(courses);

                students.add(name);
                students.add(id);
                students.add(courses);
                List<String> list = new ArrayList<>();
                list.addAll(students);

                System.out.println("do you want to continue? Y/N");
                String a=scanner.nextLine();
                if (a.equalsIgnoreCase("N")) {
                    System.out.println("Registered students");
                    for (int i = 0; i < list.size(); i++) {
                        System.out.print(list.get(i));
                    }

                    break;
                }
            }    
            
            }        
        }
    }
 