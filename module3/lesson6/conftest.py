# File with declaration of fixtures uses in this and child dir
# pytest import this file on ones own
import configparser

import pytest
from selenium import webdriver

rep_name = 'stepik_auto_tests_course'
config_name = 'firefox.ini'
rep_abs_path = __file__[:__file__.find(rep_name) + len(rep_name) + 1]
config_abs_path = f"{rep_abs_path}{config_name}"
Config = configparser.ConfigParser()
Config.read(config_abs_path)
firefox_driver_path = f"{rep_abs_path}{Config['firefox']['firefox_driver_path']}"
firefox_exe_path = Config['firefox']['firefox_exe_path']


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox(executable_path=firefox_driver_path, firefox_binary=firefox_exe_path)
    yield browser
    browser.quit()
