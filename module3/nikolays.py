import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import configparser
import time
import os


def setUp():
    config = configparser.ConfigParser()
    config.read(f"{os.path.dirname(__file__)}\\..\\firefox.ini")
    firefox_driver_path = f"{os.path.dirname(__file__)}\\..\\{config['firefox']['firefox_driver_path']}"

    browser = webdriver.Firefox(executable_path=firefox_driver_path,
                                     firefox_binary=config["firefox"]["firefox_exe_path"])
    return browser

def cry(browser):
    browser.get('http://boobooka.com/zvuki/zvuki-lyudej/zvuki-stonov/')
    browser.execute_script(
        "document.title = 'КОЛЯ ИДИ НАХУИ'; \
        document.getElementsByTagName('img')[0].src='https://i.ytimg.com/vi/xk9JRZZJJ2w/maxresdefault.jpg'; \
        document.getElementsByTagName('h1')[0].style.display='none'")
    browser.find_element_by_css_selector("[aria-controls='mep_0'][title='Воспроизвести']").click()
    time.sleep(20)


def main():
    browser = setUp()
    try:
        browser.implicitly_wait(5)
        browser.get('https://i.ytimg.com/vi/xk9JRZZJJ2w/maxresdefault.jpg')
        browser.execute_script("alert('Привет Николаус, ты пидор!\\nНажми ок чтобы подтвердить это и продолжить');")
        WebDriverWait(browser, 30).until_not(expected_conditions.alert_is_present())
        cry(browser)
    except selenium.common.exceptions.TimeoutException:
        browser.switch_to.alert.accept()
        browser.execute_script(
            "alert('Все мы знаем что ты пидор, нет смысла игнорировать этот факт\\nЯ сам нажму ок');")
        time.sleep(5)
        browser.switch_to.alert.accept()
        cry(browser)
    finally:
        browser.quit()
        print('Shut up bitch!\nЭто конец!')


if __name__ == '__main__':
    main()
