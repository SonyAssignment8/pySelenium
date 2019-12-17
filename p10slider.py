from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")
driver.implicitly_wait(12)
driver.maximize_window()
driver.switch_to.frame(0)
ele =driver.find_element_by_xpath("//div[@id='slider']/span")
ele1=driver.find_element_by_tag_name("body")
a=ActionChains(driver)
a.drag_and_drop_by_offset(ele,100,0).perform()
time.sleep(8)





