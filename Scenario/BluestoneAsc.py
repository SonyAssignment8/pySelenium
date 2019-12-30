'''Scenario 6
1. Open Browser
2. Pass URL (Bluestone)
3. Move Cursor to Rings Menu
4. Select Diamond Rings and click on it
5. Get Prise list By default
6. Select sort by and Select price low to high
7. Get Prise list price low to high
8. Compare By default price and Sorted price
9. and Verify sorted price should in ascending order. '''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
l1=[]
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.bluestone.com/")
ele=driver.find_element_by_xpath("//a[text()='Rings ']")
click_ele=driver.find_element_by_xpath("//a[text()='Diamond']")
ActionChains(driver).move_to_element(ele).perform()
ActionChains(driver).click(click_ele).perform()
lst_price=driver.find_elements_by_xpath("//span[@class='p-wrap']//span[@id='bst-discounted-price']")
for i in lst_price:
    price1=l1.append(i.text.replace("RS.","").replace(",",""))
print(l1)
l2=[]
time.sleep(4)
ele=driver.find_element_by_xpath("//span[@class='view-by-wrap title style-outline i-right']")
ActionChains(driver).move_to_element(ele).perform()
ele_price=driver.find_element_by_xpath("//a[text()='Price Low to High ']")
ActionChains(driver).click(ele_price).perform()
lst_sorted_price=driver.find_elements_by_xpath("//span[@class='p-wrap']//span[@class='new-price']")
for j in lst_sorted_price:
    price2=l2.append(j.text.replace("RS.","").replace(",",""))
print(l2)