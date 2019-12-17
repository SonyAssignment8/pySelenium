from selenium.webdriver.android import webdriver
# it will prform one time with multiple opr


def browser():
    print("driver=webdriver.Chrome()")
    print("driver.get(\"hghsadgsgjh\")")
    yield "driver"
    print("driver.close()")
    yield True


def test_1(driver):
    print("test case ex", driver)


shag = browser()
i = iter(shag)

driver = next(i)
i = iter(shag)
driver=next(i)
test_1(driver)
test_1(driver)
test_1(driver)
next(i)





