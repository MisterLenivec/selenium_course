from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    res = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(res)

    checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True

finally:
    time.sleep(10)
    browser.quit()
