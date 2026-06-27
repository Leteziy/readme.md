import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class Calculator:
    """
    Это класс для работы со страницей калькулятора, он содержит локаторы элементов и методы работы с ними
    """
    delay_element = (By.ID, "delay")
    number_7 = (By.XPATH, "//span[text()='7']")
    sign_plus = (By.XPATH, "//span[text()='+']")
    number_8 = (By.XPATH, "//span[text()='8']")
    sign_equal = (By.XPATH, "//span[text()='=']")
    display_locator = (By.CLASS_NAME, "screen")

    def __init__(self, driver: WebDriver, url: str) -> None:
        """
        Эта функция для работы с браузером и URL-адресом страницы калькулятора
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 48)

    @allure.step("Открыть страницу калькулятора")
    def open_calculator_page(self) -> None:
        """
        Эта функция открывает веб-страницу - Калькулятор
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку выполнения в сек.")
    def delay(self, seconds: str) -> None:
        """Эта функция находит поле ввода. При вписании в него числа, калькулятор
        ждет обозначенное время и только потом выводит результат"""
        delay = self.driver.find_element(*self.delay_element)
        delay.clear()
        delay.send_keys(seconds)

    @allure.step("Ввод выражения: 7+8=")
    def EnteringNumbers(self) -> None:
        """Эта функция отвечает за ввод примера и его решение"""
        self.driver.find_element(*self.number_7).click()
        self.driver.find_element(*self.sign_plus).click()
        self.driver.find_element(*self.number_8).click()
        self.driver.find_element(*self.sign_equal).click()

    @allure.step("Ожидание вывода результата")
    def result(self, expected_text: str) -> bool:
        """
        Эта функция отвечает за ожидание перед выводом результата на страницу
        """
        return self.wait.until(EC.text_to_be_present_in_element(self.display_locator, expected_text))
