import pytest

@pytest.yield_fixture()
def setUp():
    print("run before every method")
    yield
    print("run after every method")

@pytest.yield_fixture(scope="module")
def oneTimeSetUp(browser,osType):
    print("------run before onetime setup every method-----")
    if browser == 'firefox':
        print("its running on FF")
    else:
        print("its running on Chrome")
    yield
    print("---run after onetime setup every method---")

def pytest_addoption(parser):
    parser.addoption("--browser",help="to run on different browser")
    parser.addoption("--osType",help="type of os")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")