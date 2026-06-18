from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    delay_element = (By.ID, "delay")
    number_7 = (By.XPATH, "//span[text()='7']")
    sign_plus = (By.XPATH, "//span[text()='+']")
    number_8 = (By.XPATH, "//span[text()='8']")
    sign_equal = (By.XPATH, "//span[text()='=']")
    display_locator = (By.CLASS_NAME, "screen")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 48)

    def open_calculator_page(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay(self, seconds: str):
        delay = self.driver.find_element(*self.delay_element)
        delay.clear()
        delay.send_keys(seconds)

    def EnteringNumbers(self):
        self.driver.find_element(*self.number_7).click()
        self.driver.find_element(*self.sign_plus).click()
        self.driver.find_element(*self.number_8).click()
        self.driver.find_element(*self.sign_equal).click()

    def result(self, expected_text: str):
        return self.wait.until(EC.text_to_be_present_in_element(self.display_locator, expected_text))
