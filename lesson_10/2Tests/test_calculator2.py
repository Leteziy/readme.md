import allure
from selenium import webdriver
from lesson_10.PagesNew.CalcPage import Calculator


@allure.title("Тест вычисления примера 7 + 8 на веб-калькуляторе")
@allure.description("Проверяет корректность сложения чисел с заданной задержкой.")
@allure.feature("Математика")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_execution():
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    calc = Calculator(driver, url)

    calc.open_calculator_page()
    calc.delay("45")
    calc.EnteringNumbers()

    with allure.step("Проверить, что итоговый результат равен 15"):
        assert calc.result("15")

    with allure.step("Закрыть браузер"):
        driver.quit()
