from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.find_element_by_xpath("//a[text()='Droppable']").click()
driver.switch_to.frame(0)
drg=driver.find_element_by_id("draggable")
drp=driver.find_element_by_id("droppable")

ActionChains(driver).drag_and_drop(drg,drp).perform()
