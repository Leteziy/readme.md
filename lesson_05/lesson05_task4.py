from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()
text = driver.find_element(By.ID, "flash")
print("Вывод текста с зеленой плашки:")
print(text.text.strip())
driver.quit()
