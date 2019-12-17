import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()
driver.find_element_by_xpath("//a[contains(text(),'Droppable')]").click()
driver.switch_to.frame(0)
try:
    dragObj = driver.find_element_by_xpath("//div[@id='draggable']")
    dropObj = driver.find_element_by_xpath("//div[@id='droppable']")
    actions = ActionChains(driver)
    actions.drag_and_drop(dragObj, dropObj).perform()
except:
    print("not able to drop")
finally:
    driver.close()
