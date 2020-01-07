import pytest

@pytest.yield_fixture()
def setUp():
    print("before")
    yield
    print("after")

def test_m1(setUp):
    print("m1")

def test_m2(setUp):
    print("m2")