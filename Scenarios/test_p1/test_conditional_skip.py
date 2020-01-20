import pytest

a = 2
b = 3

@pytest.mark.skipiof(a<b,reason="a is 2 and b is 3")
def test_m1():
    print("test1")
def test_m2():
    print("skipped")
