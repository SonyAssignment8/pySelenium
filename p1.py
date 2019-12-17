from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def invoke_browser(func):
    def inner(url):
        driver = webdriver.Chrome(executable_path="C:/Users/ankita/AppData/Local/Programs/Python/Python35/Scripts/chromedriver.exe")
        driver.get(url)

        func(driver)
        driver.maximize_window()
        driver.close()
    return inner

@invoke_browser
def test1(driver):
    #driver.find_element_by_name("email").send_keys("ankita")
    print("test 1 executed")

@invoke_browser
def test2(driver):
    #driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("iphone")
    print("test 2 executed")

@invoke_browser
def test3(driver):
    try:
        driver.implicitly_wait(20)
        driver.find_element_by_name("identifier").send_keys("xyz")
        driver.find_element_by_xpath("//span[text()='Next']").click()
        driver.find_element_by_name("password").send_keys("")
        driver.find_element_by_xpath("//span[text()='Next']").click()
        print("test 3 executed")
    except:
        print("Exception is raised")

@invoke_browser
def test4(driver):
    #driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("iphone")
    print("test 4 executed")

@invoke_browser
def test5(driver):
    #driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("iphone")
    print("test 5 executed")


test1("https://www.facebook.com")

test2("https://www.amazon.in")

test3("https://www.gmail.com")
test4("https://www.bluestone.com")

test5("https://www.myntra.com")


