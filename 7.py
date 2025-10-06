#Write a program using Selenium WebDriver to provide the total number of objects present or available on a web page. Perform object identification and counting

package qqqqqq;

import java.util.List;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.firefox.FirefoxDriverLogLevel;

public class llll {

    public static void main(String[] args) {
        System.setProperty("webdriver.gecko.driver",
                "C:\\Users\\aman1\\OneDrive\\Documents\\geckodriver.exe");

        FirefoxOptions options = new FirefoxOptions();
        options.setLogLevel(FirefoxDriverLogLevel.ERROR);
        options.addPreference("dom.webnotifications.enabled", false);
        options.addPreference("dom.push.enabled", false);
        options.addPreference("media.autoplay.default", 1);
        options.addPreference("privacy.trackingprotection.enabled", true);

        WebDriver driver = new FirefoxDriver(options);
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

        driver.get("https://wikipedia.com");

        List<WebElement> buttons = driver.findElements(By.tagName("button"));
        System.out.println("The number of buttons is " + buttons.size());

        List<WebElement> inputs = driver.findElements(By.tagName("input"));
        System.out.println("The number of input fields is " + inputs.size());

        for (WebElement button : buttons) {
            System.out.println("Button text: " + button.getText());
        }

        for (WebElement input : inputs) {
            System.out.println("Input type: " + input.getAttribute("type"));
        }

        driver.quit();
    }
}