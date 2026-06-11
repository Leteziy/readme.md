from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # noqa: E501


driver.get("https://ya.ru/")
driver.maximize_window()

sleep(8000)
driver.save_screenshot("./ya.png")
