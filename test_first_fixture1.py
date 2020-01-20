import pytest

@pytest.fixture()
def setUp():
    print("i am fixture")

def test_method1(setUp):
    print("first method")

def test_m2thod2(setUp):
    print("method")

