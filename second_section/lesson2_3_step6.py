from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    time.sleep(1)
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    res = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(res)

    button = browser.find_element_by_tag_name("button")
    button.click()

    alert = browser.switch_to.alert
    alert_code = alert.text.split(': ')[-1]
    print(alert_code)
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()
