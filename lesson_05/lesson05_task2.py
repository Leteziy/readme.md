from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")
driver.maximize_window()
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()
print("Кликнуть по синей кнопке")
