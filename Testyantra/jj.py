# from selenium.webdriver.android import webdriver
from selenium import webdriver

def invoke_browser(func):
    def inner(url):
        driver = webdriver.Chrome(r"D:\Python\chromedriver.exe")
        driver.get(url)
        func(driver)
        driver.close()
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