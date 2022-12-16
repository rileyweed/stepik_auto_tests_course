from modules.config import FIREFOX_OPTIONS, FIREFOX_SERVICE, CHROME_OPTIONS, CHROME_SERVICE
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="firefox",
                     help="Choose browser: chrome or firefox")



@pytest.fixture(scope="function", autouse=False)
def browser(request):
    browser_name = request.config.getoption("browser")
    if browser_name == 'firefox':
        browser = webdriver.Firefox(options=FIREFOX_OPTIONS, service=FIREFOX_SERVICE)
    elif browser_name == 'chrome':
        browser = webdriver.Chrome(options=CHROME_OPTIONS, service=CHROME_SERVICE)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    yield browser
    browser.quit()
