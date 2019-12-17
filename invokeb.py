def invoke_browser(func):
    def inner(url):
        print("driver= Webdrivr.Chrome()")
        print("driver.get({})".format(url))
        func("driver")
        print("driver.close()")
    return inner

@invoke_browser
def test_1(driver):
    print("tc 1 running using ", driver)

@invoke_browser
def test_2(driver):
 print("tc 1 running using ", driver)
test_1("http://www.facebook.com")
print("---------------------------")
test_2("http://www.facebook.com")