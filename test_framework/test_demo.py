import pytest
@pytest.fixture()
def setUp():
    print("it will run only once before every methods")
def test_m1(setUp):
    print("hi")
def test_m2(setUp):
    print("hello")

