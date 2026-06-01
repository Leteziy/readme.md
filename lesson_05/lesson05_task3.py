from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")
driver.maximize_window()
input = driver.find_element(By.TAG_NAME, "input")
input.send_keys("12345")
input.clear()
input.send_keys("54321")
driver.quit()
