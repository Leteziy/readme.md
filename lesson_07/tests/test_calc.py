from selenium import webdriver
from lesson_07.pages.CalculatorPage import Calculator


def test_calculator_execution():
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    calc = Calculator(driver, url)

    calc.open_calculator_page()
    calc.delay("45")
    calc.EnteringNumbers()

    assert calc.result("15")
    driver.quit()
