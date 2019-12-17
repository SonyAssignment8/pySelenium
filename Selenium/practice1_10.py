from selenium import webdriver
import time
driver = webdriver.Chrome(r"C:\Users\Jyoti\AppData\Local\Programs\Python\Python35\Scripts\chromedriver.exe")
driver.get("http://localhost/login.do")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_name("username").send_keys("admin")
time.sleep(2)
driver.find_element_by_name("pwd").send_keys("manager")
time.sleep(2)
driver.find_element_by_id('loginButton').click()
time.sleep(2)
print(driver.title)
print(driver.current_url)
driver.minimize_window()
driver.fullscreen_window()

