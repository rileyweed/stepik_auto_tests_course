import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser
import os


class TestUniqueSelectors(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read(f"{os.path.dirname(__file__)}\\..\\firefox.ini")
        firefox_driver_path = f"{os.path.dirname(__file__)}\\..\\{config['firefox']['firefox_driver_path']}"

        self.browser = webdriver.Firefox(executable_path=firefox_driver_path,
                                         firefox_binary=config["firefox"]["firefox_exe_path"])

    def tearDown(self):
        self.browser.close()

    def fill_form(self, link):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Kea')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Lisa')
        browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('KL@google.com')

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
        return welcome_text

    def test_registration1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)


if __name__ == "__main__":
    unittest.main()
