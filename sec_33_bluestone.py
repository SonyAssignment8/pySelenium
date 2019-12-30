'''
Scenario 33
1. open browser
2. enter url(bluestone)
3. search for rings
4. click on any product
5. verify original price discount price and actual price
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
dis_price=driver.find_elements_by_xpath("//span[@id='bst-discounted-price']")
price_def=[]

#Get the list of the  defalut  price list
for i in dis_price:
    price = i.text
    price_01 = price[3:]
    price_def.append(price_01)
driver.find_element_by_xpath("//span[@class='view-by-wrap title style-outline i-right']").click()
import time
time.sleep(2)

price_act=[]
#Get the list of the  price low to high  price list
act_price=driver.find_elements_by_xpath("//span[@class='strike-price']")
for i in act_price:
    price=i.text
    price_01=price[3:]
    price_act.append(price_01)

print(price_def)
print(len(price_def))
print("============list=============")
print(price_act)
print(len(price_act))
driver.close()