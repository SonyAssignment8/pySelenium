from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.find_element_by_xpath("//a[text()='Slider']").click()
driver.switch_to.frame(0)
sldr=driver.find_element_by_xpath("//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
ActionChains(driver).drag_and_drop_by_offset(sldr,100,0).perform()
