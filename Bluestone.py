'''Scenario 5 1. Open Browser
2. Pass URL (Bluestone)
3. Move Cursor to Rings Menu
4. Select Diamond Rings and click on it
5. Get Prise list By default
6. Select sort by and Select price low to high
7. Get Prise list price low to high
8. Compare By default price and Sorted price
9. Both lists  Should vary by prices Validate here
10. Close Browser. '''
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
    price1=i.text
    l1.append(price1[3: : ])
print(l1)
l2=[]
time.sleep(4)
ele=driver.find_element_by_xpath("//span[@class='view-by-wrap title style-outline i-right']")
ActionChains(driver).move_to_element(ele).perform()
ele_price=driver.find_element_by_xpath("//a[text()='Price Low to High ']")
ActionChains(driver).click(ele_price).perform()
lst_sorted_price=driver.find_elements_by_xpath("//span[@class='p-wrap']//span[@class='new-price']")
for j in lst_sorted_price:
    price2=j.text
    l2.append(price2[3: : ])
print(l2)
for k in l1:
    l1[k]-l2[k]
    assert l2[k]!=l1[k],"False"
    print("The values are not equal")

