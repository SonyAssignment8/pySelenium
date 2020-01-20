import pytest

@pytest.mark.skip(reason="first method will skip")
def test_m1():
    print("hi")

def test_me():
    print("hello")