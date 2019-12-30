from time import sleep
import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver(request):
    driver = webdriver.Chrome()
    driver.get("https://www.netmeds.com/")
    sleep(4)

    def teardown():
        driver.close()
    request.addfinalizer(teardown)
