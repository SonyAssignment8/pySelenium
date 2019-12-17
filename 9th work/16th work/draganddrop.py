from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\chromedriver.exe')
driver.get("https://jqueryui.com/")
driver.find_element_by_xpath("//a[text()='Droppable']").click()
driver.switch_to.frame(0)
dragelement=driver.find_element_by_xpath("//div[@id='draggable']")
dropelement=driver.find_element_by_xpath("//div[@id='droppable']")
ActionChains(driver).drag_and_drop(dragelement,dropelement).perform()
