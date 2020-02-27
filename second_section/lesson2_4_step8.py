from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    book_button = browser.find_element_by_id('book')
    book_button.click()

    x = browser.find_element_by_id('input_value').text
    res = calc(x)

    answer = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(res)

    solve_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'solve'))
    ).click()

    alert = browser.switch_to.alert
    alert_code = alert.text.split(': ')[-1]
    print(alert_code)
    alert.accept()

finally:
    browser.quit()
