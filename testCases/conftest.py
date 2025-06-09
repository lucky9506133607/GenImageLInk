from selenium import webdriver
import pytest

"""@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver"""


# Run tests on Desired browser/Cross Browser/Parallel
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

#To run tests of desired browser using cmd (pytest -v -s testCases\test_login.py --browser chrome)

#To run tests parallel using cmd (pytest -v -s -n=3 testCases\test_login.py) -n=3 means how many test method do you have?


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Lucky'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Generate pytest report using cmd (pytest -v -s -n=2 --html=Reports\report.html testCases\test_login.py --browser chrome)
