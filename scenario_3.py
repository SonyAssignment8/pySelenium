from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://jqueryui.com/droppable/")
action=ActionChains(driver)
driver.switch_to_frame(0)
drag=driver.find_element_by_id("draggable")
drop=driver.find_element_by_id("droppable")
time.sleep(3)
action.drag_and_drop(drag,drop).perform()
exp_msg="Dropped!"
act_msg=drop.text
assert exp_msg.__contains__(act_msg),print("fail")
print("pass")
act_color=drop.value_of_css_property("color")
exp_color="rgba(119, 118, 32, 1)"
if exp_color==act_msg:
    print("pass")
else:
    print("fail")
