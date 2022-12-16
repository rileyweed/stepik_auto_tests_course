import pytest

class App:
    h2 = 'HELLLO'
    def __init__(self, browser):
        self.browser = browser
        self.h = 'hello_world'

@pytest.fixture()
def app(browser):
    return App(browser)


def test_1(app):
    app.browser.get("https://google.com")
    print(app.h, app.h2)
