from selenium import webdriver
def invoke_browser(func):
    print('inside invoke_browser ')
    def inner(url):
        print('inside inner')
        driver = webdriver.Chrome(r"C:\Users\Jyoti\AppData\Local\Programs\Python\Python35\Scripts\chromedriver.exe")
        driver.get(url)
        driver.maximize_window()
        func(driver)
        driver.close()

    return inner


@invoke_browser
def test_1(driver):
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_id('loginButton').click()
    print('Testcase1 executed')

# @invoke_browser
# def test_2(driver):
#     print('Testcase2 executed')
# @invoke_browser
# def test_3(driver):
#     print('Testcase3 executed')

test_1('http://localhost/login.do')
# test_2('http://localhost:8888/')
# test_3('https://www.facebook.com/')