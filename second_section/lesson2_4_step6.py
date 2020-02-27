from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('http://suninjuly.github.io/cats.html')

    button = browser.find_element_by_id('button')
    button.click()

finally:
    # Смотрим с какой ошибкой упадёт скрипт
    time.sleep(3)
    browser.quit()
