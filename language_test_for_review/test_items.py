"""
Прошу прощения, но я не буду создавать отдельный репозиторий для этого теста.
Если вы скачали полностью проект, то - cd language_test_for_review/
Раскомментируйте строку time.sleep(30) при проверке,
pytest --language=es
pytest --language=fr
Или другой поддерживаемый язык.
Можно проверить через браузеры: chrome(по умолчанию) или
firefox(нужно добавить в команду терминала --browser_name=firefox)
Спасибо.
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page_contains_a_button_to_add_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.implicitly_wait(10)
    browser.get(link)
    # time.sleep(30)

    add_btn = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'btn-add-to-basket'))
    )

    assert add_btn
