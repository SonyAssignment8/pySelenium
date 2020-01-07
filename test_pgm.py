import pytest

@pytest.fixture()
def setUp():
    print("it ll run only once before every method")
def test_m1(setUp):
    print("hi")
def test_m2(setUp,tearDown):
        print("hello")

@pytest.fixture()
def tearDown():
    print("down") #its has to be in class then we can execute




