#Write a program using Selenium WebDriver to select the number of students who have scored more than 60 in any one subject (or all subjects). Perform data extraction and analysis.

import java.io.File;
import java.io.IOException;
import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;
import org.testng.annotations.*;

public class Studentupdate {

    private static final String INPUT_FILE =
        "C:\\Users\\aman1\\OneDrive\\Documents\\student_records.xls";

    @Test
    public void testImportexport1() throws IOException, BiffException {
        File inputWorkbook = new File(INPUT_FILE);
        Workbook w;

        try {
            w = Workbook.getWorkbook(inputWorkbook);
            Sheet s = w.getSheet(0);
            int studentsAbove60 = 0;

            // Process data
            for (int i = 1; i <= 10; i++) {
                String studentStr = s.getCell(0, i).getContents();
                String marksStr = s.getCell(1, i).getContents();

                try {
                    int studentNumber = Integer.parseInt(studentStr);
                    int marks = Integer.parseInt(marksStr);

                    // Check if the marks are above 60
                    if (marks > 60) {
                        studentsAbove60++;
                        System.out.println("Student " + studentNumber +
                                           " scored above 60: " + marks);
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Invalid data for student in row " +
                                       (i + 1) + ": " + studentStr + ", " + marksStr);
                }
            }

            w.close();
            System.out.println("Number of students who scored above 60: " +
                               studentsAbove60);

        } catch (IOException | BiffException e) {
            e.printStackTrace();
        }
    }
}
