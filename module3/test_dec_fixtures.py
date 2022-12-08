import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import path
import configparser

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    config = configparser.ConfigParser()
    config.read(f"{os.path.dirname(__file__)}\\..\\fi♣6♦            ╫refox.ini")
    firefox_driver_path = f"{path.pardir}{path.sep}{config['firefox']['firefox_driver_path']}"

    browser = webdriver.Firefox(executable_path=firefox_driver_path,
                                firefox_binary=config["firefox"]["firefox_exe_path"])
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
