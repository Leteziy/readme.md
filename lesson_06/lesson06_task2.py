from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)
cookie_user1 = {
    "name": "SESSION",
    "value": "NDEzZDk0ZWUtN2VjOC00MWNiLWFhZTktOTQzNDkwOGIwMmRj",
    "domain": ".gitflic.ru",
    "path": "/",
}
cookie_user2 = {
    "name": "SESSION",
    "value": "NmRiNGFhNzktNzVkZC00NDA3LWE4YjgtM2IwMzBiODY3MzYx",
    "domain": ".gitflic.ru",
    "path": "/",
}
driver.get("https://gitflic.ru")
driver.delete_all_cookies()
driver.add_cookie(cookie_user1)
driver.refresh()
cookie_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(@class, 'cookies-alert')]//button")
    )
)
cookie_button.click()
user1L = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/user/']"))
)
user1L.click()
wait.until(EC.url_contains("/user/"))
url_user1 = driver.current_url
driver.get("https://gitflic.ru")
driver.delete_all_cookies()
driver.add_cookie(cookie_user2)
driver.refresh()
user2L = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/user/']"))
)
user2L.click()
wait.until_not(EC.url_to_be(url_user1))
url_user2 = driver.current_url
print(f"URL Пользователя 1: {url_user1}")
print(f"URL Пользователя 2: {url_user2}")
assert url_user1 != url_user2

driver.quit()
