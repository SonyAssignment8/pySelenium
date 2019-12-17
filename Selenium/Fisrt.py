from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Jyoti\AppData\Local\Programs\Python\Python35\Scripts\chromedriver.exe")
driver.get("http://localhost/login.do")
cookie = {'name': 'jyoti', 'value': 'app'}
driver.add_cookie(cookie)
cookie = (driver.get_cookies())
print(driver.get_cookie('jyoti'))
print(cookie)
driver.close()
