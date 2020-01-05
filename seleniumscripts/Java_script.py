import time

from selenium import webdriver
d=webdriver.Chrome()
d.get("https://djangobook.com/")
d.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
d.execute_script("window.scrollTo(0,document.body.scrollTop)")
