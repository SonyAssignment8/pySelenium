from selenium import webdriver
def invoke_browser(func):
    def inner(url):
        driver=webdriver.Chrome(r"C:\Users\MSN\AppData\Local\Programs\Python\Python35\Scripts\chromedriver.exe")
        driver.get(url)
        func(driver)
    return inner

@invoke_browser
def test_1(driver):
    driver.find_element_by_name("user_name").send_keys("admin")
    driver.find_element_by_name("user_password").send_keys("manager")
    driver.find_element_by_id("submitButton").click()

@invoke_browser
def test_2(driver):
    print("driver object",driver)


test_1("http://localhost:8888/")




