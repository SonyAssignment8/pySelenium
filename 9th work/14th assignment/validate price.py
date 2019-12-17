#display kurties and dresses and validate the price if it is within the range of 2000 to 5000
from selenium import webdriver
import time
driver=webdriver.Chrome("C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\chromedriver.exe")
driver.get("https://www.craftsvilla.com/")
driver.find_element_by_xpath("//a[text()='KURTIS & DRESSES ']").click()
time.sleep(3)
driver.find_element_by_xpath("//label[@title='2000-5000']").click()
time.sleep(3)
l=driver.find_elements_by_xpath("//span[@class='product-offer-price']")
for i in l:
    a=i.text
    x=int(a[2:])
    print(x)
assert x not in range (2500,5001),"False"
print("The price of the dresses are within the range")
driver.close()