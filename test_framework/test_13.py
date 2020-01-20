import pytest
@pytest.mark.run(order=5)
def test_run_order_method1(OneTimeSetup,setUp):
    print("method1")

@pytest.mark.run(order=4)
def test_run_order_method2(OneTimeSetup,setUp):
    print("method2")

@pytest.mark.run(order=1)
def test_run_order_method3(OneTimeSetup,setUp):
    print("method3")

@pytest.mark.run(order=2)
def test_run_order_method4(OneTimeSetup,setUp):
    print("method4")

@pytest.mark.run(order=3)
def test_run_order_method5(OneTimeSetup,setUp):
    print("method5")