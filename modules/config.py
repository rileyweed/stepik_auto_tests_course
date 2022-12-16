from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os

config_name = f"..{os.sep}driver.ini"
config_parser = ConfigParser()
REP_PATH = os.path.dirname(__file__)
config_parser.read(f"{REP_PATH}{os.sep}{config_name}")

FIREFOX_BINARY = config_parser["firefox"]["exe_path"]
CHROME_BINARY = config_parser["chrome"]["exe_path"]

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_argument("disable-extensions")
CHROME_OPTIONS.add_argument("--start-maximized")
CHROME_OPTIONS.add_argument("disable-infobars")
CHROME_OPTIONS.add_argument("--disable-dev-shm-usage")
CHROME_OPTIONS.add_argument("--no-sandbox")
CHROME_OPTIONS.add_argument('--ignore-certificate-errors')
CHROME_OPTIONS.add_argument('--ignore-ssl-errors')
CHROME_OPTIONS.add_experimental_option('excludeSwitches', ['enable-logging'])
CHROME_OPTIONS.binary_location = CHROME_BINARY

FIREFOX_OPTIONS = webdriver.FirefoxOptions()
# FIREFOX_OPTIONS.add_argument("disable-extensions")
# FIREFOX_OPTIONS.add_argument("--start-maximized")
FIREFOX_OPTIONS.binary_location = FIREFOX_BINARY
# preference doc - http://kb.mozillazine.org/About:config_entries#Browser
# show preference - about:config
FIREFOX_OPTIONS.set_preference("browser.download.folderList", 1)
FIREFOX_OPTIONS.set_preference("browser.download.manager.showWhenStarting", False)
FIREFOX_OPTIONS.set_preference("browser.download.manager.focusWhenStarting", False)
FIREFOX_OPTIONS.set_preference("browser.download.useDownloadDir", True)
FIREFOX_OPTIONS.set_preference("browser.helperApps.alwaysAsk.force", False)
FIREFOX_OPTIONS.set_preference("browser.download.manager.alertOnEXEOpen", False)
FIREFOX_OPTIONS.set_preference("browser.download.manager.closeWhenDone", True)
FIREFOX_OPTIONS.set_preference("browser.download.manager.showAlertOnComplete", False)
FIREFOX_OPTIONS.set_preference("browser.download.manager.useWindow", False)
# You will need to find the content-type of your app and set it here.
FIREFOX_OPTIONS.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

FIREFOX_SERVICE = FirefoxService(
    executable_path=f"{REP_PATH}{os.sep}{config_parser['firefox']['driver_path']}")

CHROME_SERVICE = ChromeService(
    executable_path=f"{REP_PATH}{os.sep}{config_parser['chrome']['driver_path']}")
