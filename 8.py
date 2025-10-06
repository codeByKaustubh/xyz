#Write a program using Selenium WebDriver to get the number of items in a list or combo box on a web page. Perform element identification and counting.

package qqqqqq;

import java.util.List;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class llll {

    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        System.setProperty("webdriver.gecko.driver",
                "C:\\Users\\aman1\\OneDrive\\Documents\\geckodriver.exe");

        // Initialize FirefoxDriver
        WebDriver driver = new FirefoxDriver();
        String url = "https://wikipedia.com";
        driver.get(url);

        // Implicit wait
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

        try {
            // Locate a combo box (select element)
            WebElement comboBox = driver.findElement(By.cssSelector("select"));

            // Find all options in the combo box
            List<WebElement> options = comboBox.findElements(By.tagName("option"));
            System.out.println("Number of items in the combo box: " + options.size());

            for (WebElement option : options) {
                System.out.println(option.getText());
            }
        } catch (Exception e) {
            System.out.println("No combo box found on the page!");
        }

        // Close the browser
        driver.close();
    }
}