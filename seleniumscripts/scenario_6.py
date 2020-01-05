from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
ring=driver.find_element_by_xpath("//a[contains(text(),'Rings ')]")
act=ActionChains(driver)
act.click_and_hold(ring).perform()
driver.find_element_by_xpath("//a[contains(text(),'Diamond Rings')]").click()
def_list=driver.find_elements_by_xpath("//span[@class='new-price']")
unsorted_lst=[]
for i in def_list:
    unsorted_lst.append(i.text.replace("RS","").replace(".","").replace(",",""))
#print(unsorted_lst)
import time
time.sleep(4)
#sort by price low to high
popular=driver.find_element_by_xpath("//span[text()=' Popular ']")
act2=ActionChains(driver)
act2.move_to_element(popular).perform()

time.sleep(5)
driver.find_element_by_xpath("//a[text()='Price Low to High ']").click()
sorted_lst1=driver.find_elements_by_id("bst-discounted-price")
sorted_lst2=[]
for j in sorted_lst1:
    sorted_lst2.append( j.text.replace("RS","").replace(".","").replace(",",""))
print(sorted_lst2)
boolean=''
for k in sorted_lst2:
    if int(k)<int(k)+1:
        boolean=True
    else:
        boolean=False
if boolean:
    print("pass")
else:
    print("Fail")
