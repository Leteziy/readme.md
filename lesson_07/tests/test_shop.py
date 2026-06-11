from selenium import webdriver
from lesson_07.pages.SwagLabsPage import Login, ShopPage, CartPage, CheckoutPage


def test_shop():
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
    assert total_text == "Total: $58.29"
    driver.quit()
