from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")

driver.find_element_by_link_text("Droppable").click()
driver.switch_to_frame(0)
drag=driver.find_element_by_id("draggable")
drop=driver.find_element_by_id("droppable")
action=ActionChains(driver)
action.drag_and_drop(drag,drop).perform()