import pytest
from selenium import webdriver
@pytest.yield_fixture()
def setUp():
    print("login to application")
    yield
    print("logout from application")


@pytest.yield_fixture(scope="module")
def OneTimeSetup(browser):
    print("lanuch browser")
    if browser=='chrome':
        driver = webdriver.Chrome()
    else:
        print("lanuch ff")
    yield
    print("close browser")

def pytest_addoption(parser):
    parser.addoption("--browser",help='to run on diff browser')
    parser.addoption("--osType",help='type of os')

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")




