from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
         driver=webdriver.Chrome()
    elif browser == 'firefox':
        driver=webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser): #value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #return the browser to setup method
    return request.config.getoption("--browser")

######### pytest HTML Report ###############

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Maram'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)