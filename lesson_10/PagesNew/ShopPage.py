import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """
    Класс, содержащий информацию, актуальную для всех страниц в тесте
    """
    def __init__(self, driver: WebDriver) -> None:
        """
        Функция, содержащая информацию о драйвере и ожидании
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


class Login(BasePage):
    """
    Класс, содержащий информацию для авторизации на сайте магазина
    """
    Username = (By.ID, "user-name")
    Password = (By.ID, "password")
    Login_button = (By.ID, "login-button")
    URL = "https://www.saucedemo.com/"

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """
        Функция открывает страницу авторизации пользователя для интернеи-магазина
        """
        self.driver.get(self.URL)

    @allure.step("Авторизация пользователя")
    def login(self, username: str, password: str) -> None:
        """
        Эта функция отвечает за авторизацию пользователя: ввод пароля и имени, клик на кнопку входа в аккаунт
        """
        self.wait.until(EC.visibility_of_element_located(self.Username)).send_keys(username)
        self.driver.find_element(*self.Password).send_keys(password)
        self.driver.find_element(*self.Login_button).click()


class ShopPage(BasePage):
    """
    Этот класс отвечает за просмотр каталога товаров и добавление их в корзину
    """
    Backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    Tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    Onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
    Cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить товары в корзину и перейти в неё")
    def add_items_to_cart(self) -> None:
        """
        Эта функция добавляет товары в корзину: рюкзак, футболка, комбинезон, и выполняет переход в корзину
        """
        self.wait.until(EC.element_to_be_clickable(self.Backpack)).click()
        self.wait.until(EC.element_to_be_clickable(self.Tshirt)).click()
        self.wait.until(EC.element_to_be_clickable(self.Onesie)).click()
        self.driver.find_element(*self.Cart_link).click()


class CartPage(BasePage):
    """
    Класс для работы со страницей корзины
    """
    Сheckout = (By.ID, "checkout")

    @allure.step("Кликнуть на кнопку оформления заказа")
    def click_checkout(self) -> None:
        """
        Нажимает кнопку перехода к оформлению заказа
        """
        self.wait.until(EC.element_to_be_clickable(self.Сheckout)).click()


class CheckoutPage(BasePage):
    """
    Этот класс работает со страницей оформления заказа
    """
    First_name = (By.ID, "first-name")
    Last_name = (By.ID, "last-name")
    Postal_code = (By.ID, "postal-code")
    Continue = (By.ID, "continue")
    Total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить данные доставки: имя, фамилия, индекс")
    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Функция отвечает за ввод персональных данных для доставки и клик на кнопку продолжения
        """
        self.wait.until(EC.visibility_of_element_located(self.First_name)).send_keys(first_name)
        self.driver.find_element(*self.Last_name).send_keys(last_name)
        self.driver.find_element(*self.Postal_code).send_keys(postal_code)
        self.driver.find_element(*self.Continue).click()

    @allure.step("Итоговая стоимость заказа")
    def total_price_text(self) -> str:
        """
        Эта функция находит на финальном экране текст с итоговой ценой и возвращает ее.
        """
        total_element = self.wait.until(EC.visibility_of_element_located(self.Total_label))
        return total_element.text
