from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

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

    browser.get('https://stepik.org/catalog?auth=login&language=ru')
    time.sleep(3)

    # Never, never don't do it!
    browser.find_element_by_id('id_login_email').send_keys('your_email')
    browser.find_element_by_id('id_login_password').send_keys('your_password')

    browser.find_element_by_class_name('sign-form__btn').click()
    time.sleep(3)
    browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
    time.sleep(3)

    textarea = browser.find_element_by_tag_name('textarea')
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)
    textarea.send_keys(alert_code)

    final_button = browser.find_element_by_class_name('submit-submission')
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           final_button)
    time.sleep(3)
    final_button.click()
    assert True

finally:
    time.sleep(10)
    browser.quit()
