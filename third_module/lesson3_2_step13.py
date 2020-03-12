from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_check_web_pages(self):
        """
        Expected fail link 2
        """
        links = [
            "http://suninjuly.github.io/registration1.html",
            "http://suninjuly.github.io/registration2.html"
        ]
        for link in links:
            self.browser = webdriver.Chrome()
            self.browser.get(link)

            div = self.browser.find_element_by_class_name('first_block')

            input1 = div.find_element_by_class_name('first')
            input1.send_keys("Ivan")
            self.assertEqual(
                'Ivan', input1.get_attribute('value'),
                'checking the input "first" value'
            )

            input2 = div.find_element_by_class_name('second')
            input2.send_keys("Petrov")
            self.assertEqual(
                'Petrov', input2.get_attribute('value'),
                'checking the input "second" value'
            )

            input3 = div.find_element_by_class_name('third')
            input3.send_keys("ivanpetrov@gmail.com")
            self.assertEqual(
                'ivanpetrov@gmail.com', input3.get_attribute('value'),
                'checking the input "third" value'
            )

            button = self.browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = self.browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual(
                welcome_text, welcome_text_elt.text,
                'welcome_text is equal welcome_text_elt.text'
            )
            self.assertEqual(
                "Congratulations! You have successfully registered!",
                welcome_text, 'text is equal welcome_text'
            )

            self.browser.quit()


if __name__ == "__main__":
    unittest.main()
