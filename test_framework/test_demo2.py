import pytest
@pytest.yield_fixture()
def setUp():
    print("it will run only once before every mtd")
    yield
    print("it will run after every method ")
def test_m1(setUp):
    print("m1")
def test_m2(setUp):
    print("m2")