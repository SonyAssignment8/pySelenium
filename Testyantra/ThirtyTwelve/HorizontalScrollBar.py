from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://djangobook.com")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollTop)")
driver.execute_script("window.scrollBy.name.length")
driver.close()