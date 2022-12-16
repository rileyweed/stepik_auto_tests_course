import pytest
from selenium.common import exceptions as ex
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math
import getpass


email = input("\ninput your email on stepik: ")
password = getpass.getpass("input your password on stepik: ")

def wait_until(browser, until, n=5):
    """
    :param browser: browser driver
    :param until: expected conditional
    :param n time of waiting
    :return: tagObject|True or False if except ex.TimeoutException
    """
    try:
        return WebDriverWait(browser, n).until(until)
    except ex.TimeoutException:
        return False


def is_visible(browser, locator, n=5, strict=False):
    """
    :param browser: browser driver
    :param locator: locator example (By.CSS_SELECTOR, "button.submit")
    :param n time of waiting
    :param strict need raise or not
    :return: tagObject or True or False if except ex.TimeoutException and not strict
    """
    conditional = EC.visibility_of_element_located(locator)
    flag = wait_until(browser, conditional, n)
    if strict and not flag:
        raise ex.TimeoutException(f"tag with {locator[0]} = '{locator[1]}' is NO VISIBLE")
    return flag


def is_clickable(browser, locator, n=5, strict=False):
    """
    :param browser: browser driver
    :param locator: locator example (By.CSS_SELECTOR, "button.submit")
    :param n time of waiting
    :param strict need raise or not
    :return: tagObject|True or False if except ex.TimeoutException and not strict
    """
    conditional = EC.element_to_be_clickable(locator)
    flag = wait_until(browser, conditional, n)
    if strict and not flag:
        raise ex.TimeoutException(f"tag with {locator[0]} = '{locator[1]}' is NO CLICKABLE")
    return flag


def reg_on_stepik(browser):
    """
    :param browser: browser driver
    :return: None
    """
    locator = (By.CSS_SELECTOR, 'a#ember33')
    is_visible(browser, locator, strict=True)
    button_enter = is_clickable(browser, locator, strict=True)
    button_enter.click()
    email_input = browser.find_element(By.CSS_SELECTOR, "form#login_form input#id_login_email")
    password_input = browser.find_element(By.CSS_SELECTOR, "form#login_form input#id_login_password")
    email_input.clear()
    email_input.send_keys(email)
    password_input.clear()
    password_input.send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "form#login_form button").click()
    # Конрольная проверка на то что нет диалогового окна для входа
    locator = (By.CSS_SELECTOR, "div.modal-dialog-bg")
    conditional = EC.invisibility_of_element_located(locator)
    flag = wait_until(browser, conditional, 5)
    if not flag:
        if is_visible(browser, (By.CSS_SELECTOR, "li[role='alert']")):
            pytest.skip("E-mail адресc и/или пароль не верны")
            return
        raise ex.TimeoutException(f"tag with {locator[0]} = {locator[1]} is visible")


def answer():
    return math.log(int(time.time()))


def check_answer(browser):
    is_visible(browser, (By.CSS_SELECTOR, "span.attempt-message_correct"), strict=True)
    p = is_visible(browser, (By.CSS_SELECTOR, "p.smart-hints__hint"), strict=True)
    answer_text = p.text
    assert answer_text == 'Correct!', f'Answer incorrect! Except Correct! got {answer_text}'


links = [
    "https://stepik.org/lesson/236895/step/1",
    # "https://stepik.org/lesson/236896/step/1",
    # "https://stepik.org/lesson/236897/step/1",
    # "https://stepik.org/lesson/236898/step/1",
    # "https://stepik.org/lesson/236899/step/1",
    # "https://stepik.org/lesson/236903/step/1",
    # "https://stepik.org/lesson/236904/step/1",
    # "https://stepik.org/lesson/236905/step/1",
]



@pytest.mark.parametrize('link', links)
def test_check_answer_on_link(browser, link):
    # задаем неявное ожидание для каждои операции
    browser.implicitly_wait(10)
    # переходим по ссылке
    browser.get(link)
    # регистрируемся на саите
    reg_on_stepik(browser)
    # textarea case________________________________________________________>
    locator = (By.CSS_SELECTOR, "textarea.ember-text-area")
    tag_textarea = is_visible(browser, locator, strict=True)
    if not is_clickable(browser, locator):
        check_answer(browser)
        return
    tag_textarea.clear()
    tag_textarea.send_keys(str(answer()))
    # button case_________________________________________________________>
    locator = (By.CSS_SELECTOR, "button.submit-submission")
    is_visible(browser, locator, strict=True)
    tag_button = is_clickable(browser, locator, strict=True)
    tag_button.click()
    # Check Answer case____________________________________________________>
    check_answer(browser)