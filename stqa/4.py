#Write a program using Selenium WebDriver to automate the log in process on a specific webpage. Verify successful login with appropriate assertions.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
options=Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
print("Testing started")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
sleep(3)
title=driver.title
print(f"Page title is {title}")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
sleep(3)
first_item = driver.find_element(By.CLASS_NAME, "inventory_item")
assert first_item.is_displayed(), "First inventory item is not displayed"
first_item_name = first_item.find_element(By.CLASS_NAME, "inventory_item_name").text
print(f"First item name: {first_item_name}")
print("Test passed, your LOGIN is successful and first inventory item is verified")
driver.quit()