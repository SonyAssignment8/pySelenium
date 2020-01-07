'''Scenario 8
1. open Browser
2. Pass Url (bluestone)
3. Move the cursor All Jewellery
4. select Kadas and click on it
5. select any kada.
6. Select Bangle size
7. click on buy now
8. capture the size of item in cart page and Compare with selectd size '''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
l1=[]
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.bluestone.com/")
ele=driver.find_element_by_xpath("//a[text()='All Jewellery ']")
click_ele=driver.find_element_by_xpath("//a[text()='Kadas']")
ActionChains(driver).move_to_element(ele).perform()
ActionChains(driver).click(click_ele).perform()
parent=driver.window_handles[0]
driver.find_element_by_xpath("//img[@alt='The Abijeet Kada For Him']").click()
child=driver.window_handles[1]
driver.switch_to.window(child)
driver.find_element_by_xpath('''//span[@class='size-box-overlay']''').click()
Exp_sel_size=driver.find_element_by_xpath('''//span[text()='2-2(2 2/16")']''').text
sel_size=driver.find_element_by_xpath('''//span[text()='2-2(2 2/16")']''')
sel_size.click()
time.sleep(4)
driver.find_element_by_xpath("//input[@id='buy-now']").click()
Act_sel_size=driver.find_element_by_xpath('''//span[text()='2-2(2 2/16")']''').text
assert Exp_sel_size==Act_sel_size,"False"
print("The size of the selected bangle is validated------>Pass")
