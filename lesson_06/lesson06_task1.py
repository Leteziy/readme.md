from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    start_button.click()

    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
    )

    driver.save_screenshot("result.png")

    finish = driver.find_element(By.ID, "finish")
    assert finish.text == "Hello World!"

    driver.quit()
