import allure
from selenium import webdriver
from lesson_10.PagesNew.ShopPage import Login, ShopPage, CartPage, CheckoutPage


@allure.title("Тест оформления покупки в онлайн-магазине Swag Labs")
@allure.description("Авторизация, добавляе три товара в корзину, оформляет заказ и проверяет финальную стоимость.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop() -> None:
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = Login(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    shop_page = ShopPage(driver)
    shop_page.add_items_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_shipping_info("Елизавета", "Котрова", "011160")

    total_text = checkout_page.total_price_text()

    with allure.step("Проверить, что финальная стоимость равна $58.29"):
        assert total_text == "Total: $58.29"
    with allure.step("Закрыть браузер"):
        driver.quit()
