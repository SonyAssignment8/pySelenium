#jquery slider
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\chromedriver.exe')
driver.get("https://jqueryui.com/")
driver.find_element_by_xpath("//a[text()='Slider']").click()
driver.switch_to.frame(0)
ele=driver.find_element_by_xpath("//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
ActionChains(driver).drag_and_drop_by_offset(ele,100,0).perform()