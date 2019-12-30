from selenium import webdriver
#from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://www.bluestone.com/")
driver.implicitly_wait(12)
driver.maximize_window()
move=driver.find_element_by_xpath("//a[text()='Rings ']")
a=ActionChains(driver)
a.move_to_element(move).perform()
time.sleep(9)
driver.find_element_by_link_text("Diamond").click()
time.sleep(5)
lst=driver.find_elements_by_xpath("//span[@id='bst-discounted-price']")
price_def=[]

#get the list  of the default price list
for i in lst:
    price =i.text
    price_1=price[3:]
    price_def.append(price_1)
driver.find_element_by_xpath("//span[@class='view-by-wrap title style-outline i-right']").click()

import time
time.sleep(2)
driver.find_element_by_xpath("//div[@class='form-item ']//a[contains(text(),'Price Low to High')]").click()
price_lowhigh=[]

#get the list  of the low to high price list
d_lst=driver.find_elements_by_xpath("//span[@id='bst-discounted-price']")
for i in d_lst:
    price =i.text
    price_1=price[3:]
    price_lowhigh.append(price_1)
print(price_def)
print(len(price_def))
print("##########################")
print(price_lowhigh)
print(len(price_lowhigh))

#convet list into string to remove the ","
str_price_def=str(price_def)
print(str_price_def.replace(",",""))
print("********************")
str_price_loh=str(price_def)
print(str_price_loh.replace(",",""))
print("ascending order list",price_lowhigh.sort())
print("********************")
driver.close()

