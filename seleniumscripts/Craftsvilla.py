from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.craftsvilla.com/")
driver.find_element_by_xpath("//a[contains(text(),'KURTIS & DRESSES ')]").click()
time.sleep(5)
driver.find_element_by_xpath("//label[@for='price_2000-5000']").click()
time.sleep(2)
list=driver.find_elements_by_xpath("//span[@class='product-offer-price']")
time.sleep(2)
for i in list:
    print(i.text)
