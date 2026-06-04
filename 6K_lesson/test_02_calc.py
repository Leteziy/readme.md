from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  # noqa: E501

    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait = WebDriverWait(driver, 48)
    display_locator = (By.CLASS_NAME, "screen")

    result = wait.until(EC.text_to_be_present_in_element(display_locator, "15"))  # noqa: E501

    assert result

    driver.quit()
