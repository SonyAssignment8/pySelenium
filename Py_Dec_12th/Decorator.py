# Decorator
from selenium import webdriver
import time

def invoke_browser(func):
    def inner(url):
        driver = webdriver.Chrome()
        driver.get(url)
        func(driver)
        driver.close()

    return inner

driver1 = webdriver.Chrome()
@invoke_browser
def test_1(driver):
    driver.find_element_by_id("email").send_keys("revannand@gmail.com")
    driver.find_element_by_id("pass").send_keys("Dhanya@0419")
    time.sleep(5)
    driver.find_element_by_id("u_0_b").click()



@invoke_browser
def test_2(driver):
    print("test case2 running using")


test_1("https://www.facebook.com")
print("----------------------------")
#test_2("https://www.gmail.com")
