from selenium.webdriver.android import webdriver
def browser():
    print("driver=webdriver.Chrome()")
    print("driver.get(\"hghsadgsgjh\")")
    yield "driver"
    print("driver.close()")
    yield True

def test_1(driver):
    print("test case ex", driver)
shag=browser()
i = iter(shag)

driver = next(i)
i=iter(shag)
next(i)

driver = next(i)
i=iter(shag)
next(i)

driver = next(i)
i=iter(shag)
next(i)

driver = next(i)
i=iter(shag)
next(i)



