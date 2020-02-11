import pytest
from selenium import webdriver
from source.utilities.webdriver_factory import WebDriverFactory


@pytest.yield_fixture(scope="class")
def OneTimeSetup(request,browser):
    wdf=WebDriverFactory(browser)
    driver=wdf.getWebDriverInstance()

    if request.cls is not None:
       request.cls.driver=driver
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")





