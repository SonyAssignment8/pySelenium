from selenium import  webdriver
#from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://jqueryui.com/")

#drag and drop
# driver.find_element_by_link_text("Droppable").click()
# driver.switch_to_frame(0)
# drag=driver.find_element_by_id("draggable")
# drop=driver.find_element_by_id("droppable")
# action=ActionChains(driver)
# action.drag_and_drop(drag,drop).perform()

#drag mouse cursor to y axis in sliding
driver.find_element_by_link_text("Slider").click()
a=driver.find_element_by_class_name("demo-frame")
driver.switch_to_frame(a)
b=driver.find_element_by_id("slider")
action=ActionChains(driver)
action.drag_and_drop_by_offset(b,100,0).perform()
