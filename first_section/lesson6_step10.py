from selenium import webdriver
import time


try: 
    # link = "http://suninjuly.github.io/registration1.html"
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    div = browser.find_element_by_class_name('first_block')

    input1 = div.find_element_by_class_name('first')
    input1.send_keys("Ivan")
    input2 = div.find_element_by_class_name('second')
    input2.send_keys("Petrov")
    input3 = div.find_element_by_class_name('third')
    input3.send_keys("ivanpetrov@gmail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
