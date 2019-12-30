from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.google.com/")
time.sleep(10)
driver.get("https://demo.actitime.com/login.do")
driver.execute_script('window.open(("https://demo.actitime.com/login.do"),"tab2")')
driver.switch_to_window('tab2')
driver.save_screenshot("sample.png")
driver.close()

