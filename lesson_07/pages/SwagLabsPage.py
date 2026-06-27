from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


class Login(BasePage):
    Username = (By.ID, "user-name")
    Password = (By.ID, "password")
    Login_button = (By.ID, "login-button")
    URL = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.Username)).send_keys(username)
        self.driver.find_element(*self.Password).send_keys(password)
        self.driver.find_element(*self.Login_button).click()


class ShopPage(BasePage):
    Backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    Tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    Onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
    Cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_items_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.Backpack)).click()
        self.wait.until(EC.element_to_be_clickable(self.Tshirt)).click()
        self.wait.until(EC.element_to_be_clickable(self.Onesie)).click()
        self.driver.find_element(*self.Cart_link).click()


class CartPage(BasePage):
    Сheckout = (By.ID, "checkout")

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.Сheckout)).click()


class CheckoutPage(BasePage):
    First_name = (By.ID, "first-name")
    Last_name = (By.ID, "last-name")
    Postal_code = (By.ID, "postal-code")
    Continue = (By.ID, "continue")
    Total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_shipping_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located(self.First_name)).send_keys(first_name)
        self.driver.find_element(*self.Last_name).send_keys(last_name)
        self.driver.find_element(*self.Postal_code).send_keys(postal_code)
        self.driver.find_element(*self.Continue).click()

    def total_price_text(self):
        total_element = self.wait.until(EC.visibility_of_element_located(self.Total_label))
        return total_element.text
