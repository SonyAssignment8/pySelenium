from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.urbanladder.com/")
driver.implicitly_wait(10)
driver.maximize_window()
lst = driver.find_elements_by_xpath("//div[@id='topnav_wrapper']/ul/li")
for j in lst:
    if j.text == "Living":
        j.click()

list1 = driver.find_elements_by_xpath("//div[@class='subnavlist lt']")
for k in list1:
    print(k.text)

