from selenium.common import exceptions as ex
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def wait_until(browser, until, n=5, strict=False):
    """
    :param browser: browser driver
    :param until: expected conditional
    :param n time of waiting
    :return: tagObject|True or False if except ex.TimeoutException and not strict
    """
    try:
        return WebDriverWait(browser, n).until(until)
    except ex.TimeoutException:
        if strict:
            raise ex.TimeoutException(f"NO {until}")
        return False


def is_visible(browser, locator, n=5, strict=True):
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


def is_clickable(browser, locator, n=5, strict=True):
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
