import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store_true', help='enable headless mod for supported browsers.')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        print(' \nStart browser chrome for test')
        options = Options()
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser_name == 'firefox':
        print(' \nStart browser firefox for test')
        fp = webdriver.FirefoxProfile()
        driver = webdriver.Firefox(firefox_profile=fp)
        driver.implicitly_wait(5)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield driver
    print('\nBroser closed for test')
    driver.quit()