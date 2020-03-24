from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('number', [
    "236895",
    "236896",
    "236897",
    "236898",
    "236899",
    "236903",
    "236904",
    "236905"
])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1'"
    browser.implicitly_wait(10)
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'textarea'))
    ).send_keys(str(math.log(int(time.time()))))

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
    ).click()

    hint = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
    )

    try:
        assert hint.text == 'Correct!', 'check result is correct'
    except AssertionError:
        print(hint.text)
