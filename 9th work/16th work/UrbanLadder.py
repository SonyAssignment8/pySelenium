from selenium import webdriver
import time
driver=webdriver.Chrome('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\chromedriver.exe')
driver.get('https://www.urbanladder.com/')
time.sleep(5)
# driver.find_element_by_xpath("//a[@class='close-reveal-modal hide-mobile']").click()
lst=driver.find_elements_by_xpath("//span[@class='topnav_itemname']")
for i in lst:
    print(i.text)