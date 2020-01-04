from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/")

driver.implicitly_wait(3)
driver.find_element_by_xpath("//a[text()='Slider']").click()
driver.switch_to.frame(0)
scr=driver.find_element_by_xpath("//div[@id='slider']")
act=ActionChains(driver)
act.drag_and_drop_by_offset(scr,225,0).perform()
act.drag_and_drop_by_offset(scr,0,0).perform()
act.drag_and_drop_by_offset(scr,-100,0).perform()
act.drag_and_drop_by_offset(scr,-175,0).perform()
act.drag_and_drop_by_offset(scr,-225,0).perform()
driver.close()
