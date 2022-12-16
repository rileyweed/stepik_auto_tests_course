import configparser
import os
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def cry(browser):
    browser.get('http://boobooka.com/zvuki/zvuki-lyudej/zvuki-stonov/')
    browser.execute_script(
        "document.title = 'КОЛЯ ИДИ НАХУИ'; \
        document.getElementsByTagName('img')[0].src='https://i.ytimg.com/vi/xk9JRZZJJ2w/maxresdefault.jpg'; \
        document.getElementsByTagName('h1')[0].style.display='none'")
    browser.find_element(By.CSS_SELECTOR, "[aria-controls='mep_0'][title='Воспроизвести']").click()
    time.sleep(20)


def test_main(browser):
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
