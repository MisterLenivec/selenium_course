from selenium import webdriver
import time
import os


try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('Такой-то')

    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Такойтович')

    email = browser.find_element_by_name('email')
    email.send_keys('takoito@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'something.txt')

    element = browser.find_element_by_id('file')
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True

finally:
    time.sleep(10)
    browser.quit()
