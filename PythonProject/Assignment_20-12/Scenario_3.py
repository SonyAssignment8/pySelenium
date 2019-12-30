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

exp_bckGrndClr = "rgba(255, 250, 144, 1)"
act_bckGrndClr = driver.find_element_by_id("droppable").value_of_css_property('background-color')
assert exp_bckGrndClr == act_bckGrndClr, "Background color not verified"
print("Background color is verified")

exp_txt = "Dropped!"
act_txt = driver.find_element_by_xpath("//div/p[text()='Dropped!']").text
assert exp_txt == act_txt, "Text not verified"
print("Text verified")
