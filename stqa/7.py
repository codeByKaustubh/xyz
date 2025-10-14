from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
try:
    driver.get("https://www.w3schools.com/")
    driver.maximize_window()
    time.sleep(2)
    elements = driver.find_elements(By.XPATH, "//*")
    total_objects = len(elements)
    print(f"Total number of objects (HTML elements) on this page: {total_objects}")
finally:
    driver.quit()