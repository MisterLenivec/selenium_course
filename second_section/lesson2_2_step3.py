from selenium import webdriver
import time

from selenium.webdriver.support.ui import Select


def calc(x, y):
    return str(int(x) + int(y))


try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    res = calc(x, y)

    # browser.find_element_by_id('dropdown').click()
    # browser.find_element_by_css_selector("[value='{}']".format(res)).click()

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(res)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
