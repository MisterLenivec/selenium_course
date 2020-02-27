from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id('treasure')
    x = treasure.get_attribute('valuex')
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    robot_checkbox.click()

    robot_radio = browser.find_element_by_id('robotsRule')
    robot_radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
