'''
Scenario 6
 1. Open Browser
  2. Pass URL (Bluestone)
   3. Move Cursor to Rings Menu
   4. Select Diamond Rings and click on it
    5. Get Prise list By default
    6. Select sort by and Select price low to high
     7. Get Prise list price low to high
     8. Compare By default price and Sorted price
      9. and Verify sorted price should in ascending order.
      10. Close Browser
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
ring_we=driver.find_element_by_xpath("//a[contains(text(),'Rings ')]")
act=ActionChains(driver)
act.click_and_hold(ring_we).perform()
driver.find_element_by_xpath("//div[text()='Popular Ring Types ']/../../..//ul//li//a[text()='Diamond']").click()
def_list=driver.find_elements_by_xpath("//span[@id='bst-discounted-price']")
price_def=[]

#Get the list of the  defalut  price list
for i in def_list:
    price = i.text
    price_01 = price[3:]
    price_def.append(price_01)
driver.find_element_by_xpath("//span[@class='view-by-wrap title style-outline i-right']").click()
import time
time.sleep(2)
driver.find_element_by_xpath("//div[@class='form-item ']//a[contains(text(),'Price Low to High')]").click()
price_lowrohigh=[]
#Get the list of the  price low to high  price list
def_list=driver.find_elements_by_xpath("//span[@id='bst-discounted-price']")
for i in def_list:
    price=i.text
    price_01=price[3:]
    price_lowrohigh.append(price_01)

print(price_def)
print(len(price_def))
print("============list=============")
print(price_lowrohigh)
print(len(price_lowrohigh))
print("=======================================")
sort_list_def=price_def.sort()
sort_list_ltoh=price_lowrohigh.sort()
assert price_def==sort_list_def and price_lowrohigh==sort_list_ltoh,"prices not matched"
print("Prices are matched")
driver.close()