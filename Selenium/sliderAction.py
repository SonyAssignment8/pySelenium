import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.implicitly_wait(20)
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='Slider']").click()
driver.switch_to.frame(0)
wb = driver.find_element_by_xpath("//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
act = ActionChains(driver)
act.drag_and_drop_by_offset(wb,100,0).perform()