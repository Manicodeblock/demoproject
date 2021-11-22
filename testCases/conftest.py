from selenium import webdriver
import pytest
from termcolor import colored
@pytest.fixture()
def setup(browser):
    global driver
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="/home/ticvictech/PycharmProjects/nopcommerceProject/Drivers/chromedriver")
        print("Launching Chrome browser")
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path="/home/ticvictech/PycharmProjects/nopcommerceProject/Drivers/geckodriver")
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome(executable_path="/home/ticvictech/PycharmProjects/nopcommerceProject/Drivers/chromedriver")
    return driver
def pytest_addoption(parser): #This method is to select the browser in CLI (run time as argument)
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):#return the browser value
    return request.config.getoption("--browser")
#htmlreport code#

#it is hook for adding environment info into HTML report
def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module name']='customer'
    config._metadata['Tester'] ='Manikandan Vinayagam'
    config._metadata['Company']='Ticvic Yechnologies pvt Ltd'
#it is hook for delete/modyfy environment info into HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Javahome",None)
    metadata.pop("Plugins",None)
#these are customisable we can adding a command

