from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
start = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "start"))
)
start.click()
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
)
finish = driver.find_element(By.ID, "finish")
driver.save_screenshot("result.png")
assert (
    finish.text == "Hello World!"
)
print(finish.text)
driver.quit()
