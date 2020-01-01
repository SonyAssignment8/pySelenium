
from selenium import webdriver
driver =webdriver.Chrome()
driver.get("http://facebook.com")
a=driver.current_window_handle
driver.save_screenshot("sample.png")
print(a)
driver.execute_script("window.open('http://taritas.com/', 'tab2')")
driver.switch_to_window('tab2')
b=driver.current_window_handle
print(b)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
import time
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollTop)")
driver.save_screenshot("sample.png")
