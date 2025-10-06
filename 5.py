#Write a program using Selenium WebDriver to update 10 student records in an Excel file. Perform data manipulation and verification

import java.io.File;
import java.io.IOException;
import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;
import jxl.write.Number;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;
import jxl.write.WriteException;
import org.testng.annotations.Test;

public class StudentUpdate {

    private static final String INPUT_FILE =
            "C:\\Users\\aman1\\OneDrive\\Documents\\student_records.xls";
    private static final String OUTPUT_FILE =
            "C:\\Users\\aman1\\OneDrive\\Documents\\student_records_updated.xls";

    @Test
    public void testImportExport() throws IOException, BiffException, WriteException {
        File inputWorkbook = new File(INPUT_FILE);
        Workbook w = null;
        WritableWorkbook copy = null;

        try {
            // Open input Excel file
            w = Workbook.getWorkbook(inputWorkbook);
            Sheet s = w.getSheet(0);

            // Create writable copy
            copy = Workbook.createWorkbook(new File(OUTPUT_FILE), w);
            WritableSheet sheet = copy.getSheet(0);

            int studentsAbove60 = 0;
            int totalRows = s.getRows();

            // Process each student record (skip header)
            for (int i = 1; i < totalRows; i++) {
                String studentStr = s.getCell(0, i).getContents().trim();
                String marksStr = s.getCell(1, i).getContents().trim();

                try {
                    int studentNumber = Integer.parseInt(studentStr);
                    int marks = Integer.parseInt(marksStr);
                    int updatedMarks = marks + 10;

                    // Write updated marks
                    Number updatedMarksCell = new Number(1, i, updatedMarks);
                    sheet.addCell(updatedMarksCell);

                    // Count students who originally scored above 60
                    if (marks > 60) {
                        studentsAbove60++;
                    }

                    System.out.println("Record updated for student " + studentNumber + ": " +
                            marks + " -> " + updatedMarks);

                } catch (NumberFormatException e) {
                    System.out.println("Invalid data at row " + (i + 1) + ": " +
                            studentStr + ", " + marksStr);
                }
            }

            // Write and close
            copy.write();
            System.out.println("\n✅ All records successfully updated!");
            System.out.println("📊 Number of students who scored above 60 (before update): " +
                    studentsAbove60);

        } catch (IOException | BiffException | WriteException e) {
            e.printStackTrace();
        } finally {
            if (copy != null) copy.close();
            if (w != null) w.close();
        }
    }
}