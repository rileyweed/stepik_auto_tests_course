import pytest
from selenium import webdriver
import os
import configparser

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage():
    def setup_class(self):
        config = configparser.ConfigParser()
        config.read(f"{os.path.dirname(__file__)}\\..\\firefox.ini")
        firefox_driver_path = f"{os.path.dirname(__file__)}\\..\\{config['firefox']['firefox_driver_path']}"

        self.browser = webdriver.Firefox(executable_path=firefox_driver_path,
                                         firefox_binary=config["firefox"]["firefox_exe_path"])

    def teardown_class(self):
        self.browser.quit()

    def setup_method(self):
        self.browser.get(link)

    def teardown_method(self):
        print('ok')

    def test_guest_should_see_login_link(self):
        self.browser.find_element_by_css_selector("#login-link")

    def test_guest_should_see_basket_link(self):
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")