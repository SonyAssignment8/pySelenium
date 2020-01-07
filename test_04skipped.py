import pytest

a=2
b=3

@pytest.mark.skipif(a<b,reason="a is 2 and b is 3")
def test_m1():
    print("hello")

def test_m2():
    print("hai")