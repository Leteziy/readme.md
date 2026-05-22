from selenium import webdriver

# Этот код сам найдет ваш Chrome, сам скачает драйвер в фоновом режиме и
# откроет сайт
driver = webdriver.Chrome()
driver.get("https://google.com")


import time
time.sleep(5)
# driver.quit()
