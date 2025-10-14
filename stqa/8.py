from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
try:
    driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
    time.sleep(2)
    driver.switch_to.frame("iframeResult")
    dropdown_element = driver.find_element(By.TAG_NAME, "select")
    select = Select(dropdown_element)
    options = select.options
    count = len(options)
    print("Items available in the combo box:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option.text}")
    print(f"\nTotal number of items in the combo box: {count}")
finally:
    driver.quit()