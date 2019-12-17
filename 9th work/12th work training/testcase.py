from selenium import webdriver
import time
def invoke_browser(func):
    def inner(url):
        driver=webdriver.Chrome("C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\chromedriver.exe")
        driver.get(url)
        func(driver)
        driver.close()
        print("test1 is closed")
    return inner

@invoke_browser
def test1(driver):
    print('test1 is executed')
    time.sleep(3)
    x_username = driver.find_element_by_id("username")
    a="admin"
    username=lambda element,a:element.send_keys(a)
    username(x_username,a)
    time.sleep(3)
    driver.find_element_by_name("pwd").send_keys("manager")
    time.sleep(3)
    driver.find_element_by_id("loginButton").click()
#
#
# @invoke_browser
# def test2(driver):
#     print('test2 is executed')
#
#
# @invoke_browser
# def test3(driver):
#     print('test3 is executed')
#
#
# @invoke_browser
# def test4(driver):
#     print('test4 is executed')
#
#
# @invoke_browser
# def test5(driver):
#     print('test5 is executed')
#
#
# @invoke_browser
# def test6(driver):
#     print('test6 is executed')
#
#
# @invoke_browser
# def test7(driver):
#     print('test7 is executed')
#
test1("http://localhost/login.do")
# test2("https://www.facebook.com/")
# test3("https://www.google.com/")
# test4("https://www.amazon.in/")
# test5("https://www.flipkart.in/")
# test6("https://www.gmail.com/")
# test7("https://www.bigbasket.com/")