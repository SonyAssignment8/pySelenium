from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
act=ActionChains(driver)
wb=driver.find_element_by_xpath("//a[text()='All Jewellery ']")
act.move_to_element(wb).perform()
driver.find_element_by_xpath("//span[text()='Kadas']").click()
driver.find_element_by_xpath("//span[@class='p-wrap'][1]").click()
sid=driver.window_handles
i=iter(sid)
pid=next(i)
cid=next(i)
driver.switch_to_window(cid)
import time
time.sleep(3)
#driver.find_element_by_xpath("//span[@class='size-box-overlay']").click
driver.find_element_by_xpath("//span[@class='size-box-overlay']").click()
driver.find_element_by_xpath("//span[contains(text(),'2-12')]").click()
size=driver.find_element_by_xpath("//span[contains(text(),'2-12')]").text
print(size)
driver.find_element_by_id("buy-now").click()
size2=driver.find_element_by_xpath("//span[contains(text(),'2-12')]").text
print(size2)
if size==size2:
    print("pass")
else:
    print("fail")