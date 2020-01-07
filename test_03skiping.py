import pytest

@pytest.mark.skip(reason="first method skip")
def test_m1(): #m1 () is skipping
    print("hi")

def test_m2():
    print("hello")