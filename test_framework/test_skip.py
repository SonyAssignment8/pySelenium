import pytest

@pytest.mark.skip(reason="please skip")
def test_m1():
    print("hi")

def test_m2():
    print("hello")