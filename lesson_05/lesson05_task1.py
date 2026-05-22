# from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")
driver.maximize_window()
time.sleep(3)
xpath_selector = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"  # noqa: E501
button = driver.find_element(By.XPATH, xpath_selector)
button.click()
ОК = driver.switch_to.alert
time.sleep(3)
ОК.accept()
print("Задание выполнено")
# sleep(30)
