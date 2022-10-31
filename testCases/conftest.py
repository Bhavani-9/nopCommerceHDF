from selenium import webdriver
import pytest

@pytest.fixture()
def setUp(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        print("******Launching chrome browser******")
    elif browser=="Firefox":
        driver=webdriver.Firefox()
        print("******Launching firefox browser******")
    return driver


def pytest_addoption(parser):                      # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                            # This will return the browser value to setup method
    return request.config.getoption("--browser")

########### pytest html report ###########

#  It is hook for adding environment info to HTML report

def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Hiral'

#  It is hook for delete/modify environment info to HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)






