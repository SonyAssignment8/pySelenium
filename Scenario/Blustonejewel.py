'''Scenario 7
 1. open Browser
 2. Pass Url (bluestone)
 3. Move the cursor  All Jewellery
4. select Kadas and click on it
5. select any kada.
6. click on buy now
7. Capture whether error message is displayed or not(Not Displayed fail test case) '''
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
time.sleep(4)
driver.find_element_by_xpath("//input[@id='buy-now']").click()
msg=driver.find_element_by_xpath("//div[text()='* This field is required']")
failed_msg=msg.text
assert msg.text==failed_msg,"False"
print("The failure message is displayed---->pass")
driver.close()
