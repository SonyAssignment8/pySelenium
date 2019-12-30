from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
time.sleep(3)
driver.add_cookie({'name':'a','value':'apple'})
print(driver.get_cookie("a"))
#driver.close()