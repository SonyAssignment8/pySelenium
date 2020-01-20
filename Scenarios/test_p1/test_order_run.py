import pytest

@pytest.mark.run(order=2)
def test_run_order_method1(onetimesetUp,setUp):
    print("method1")

@pytest.mark.run(order=1)
def test_run_order_method2(onetimesetUp,setUp):
    print("method2")

@pytest.mark.run(order=1)
def test_run_order_method3(onetimesetUp,setUp):
    print("method3")

