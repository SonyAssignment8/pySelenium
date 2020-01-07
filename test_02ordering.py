import pytest
#output :3,2,5,2,1

@pytest.mark.run(order=5)
def test_run_order_method1(oneTimeSetUp,setUp):
    print("method 1")


@pytest.mark.run(order=4)
def test_run_order_method2(oneTimeSetUp,setUp):
    print("method 2")


@pytest.mark.run(order=1)
def test_run_order_method3(oneTimeSetUp,setUp):
    print("method 3")

@pytest.mark.run(order=2)
def test_run_order_method4(oneTimeSetUp,setUp):
    print("method 4")


@pytest.mark.run(order=3)
def test_run_order_method5(oneTimeSetUp,setUp):
    print("method 5")
