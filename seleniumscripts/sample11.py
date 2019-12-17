from selenium import webdriver
def invoke_browser(func):
    def inner(url):
        driver=webdriver.Chrome("C:\\Users\\rashmi\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\chromedriver.exe")
        driver.get(url)
        func(driver)
    return inner
@invoke_browser
def test_1(driver):
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_id("loginButton").click()
test_1("http://localhost/login.do")
