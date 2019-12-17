# Urbanladder
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://www.urbanladder.com/")
links= driver.find_elements(By.XPATH, " //div[@id='topnav_wrapper']/ul/li/span")
for i in links:
    print(i.text)

