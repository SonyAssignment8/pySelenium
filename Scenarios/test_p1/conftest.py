import pytest

@pytest.yield_fixture()
def setUp():
    print("Run before for every method")
    yield
    print("Run after every methods")

@pytest.yield_fixture(scope ="module")
def onetimesetUp(browser,osType):
    print("____run only once before every method___")
    yield
    print("____run only once after very method___")

@pytest.yield_fixture(scope="module")
def onetimesetUp(browser,osType):
        print("------run before onetime setup every method---")
        if browser == 'firefox':
            print("its running on FF")
        else:
            print("its running on Chrome")
        yield
        print("-----run after onetimesetup every method---")

def pytest_addoption(parser):
    parser.addoption("--browser",help="to run on different browser")
    parser.addoption("--osType",help="type of os")

@pytest.fixture(scope="session")
def browser(request):
    return request.comnfig.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

