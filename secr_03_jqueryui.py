'''
1. Open a browser of your choice say Mozilla Firefox
2. Navigate to http://jqueryui.com/droppable/ webpage.
3. Consider “Drag me to my target” as a source and “Drop here” as a target.
 4. Write a code to perform drag and drop operation from source to target.
 5. After drag and drop verify the operation is successfully by checking the color property of CSS and also verify text change.
  (Use assert statement to verify that color and text are as expected.)
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/")
driver.find_element_by_link_text("Droppable").click()
driver.switch_to.frame(0)
wb1=driver.find_element_by_xpath("//div[@id='draggable']")
wb2=driver.find_element_by_xpath("//div[@id='droppable']")

try:
    act=ActionChains(driver)
    #act.drag_and_drop(wb1,wb2).perform()
    act.click_and_hold(wb1).move_to_element(wb2).release().perform()
except:
    print("Not able to drop")

wb=driver.find_element_by_xpath("//div[@class='ui-widget-header ui-droppable ui-state-highlight']")
act_color=wb.value_of_css_property("background-color")
act_text=wb.text
#print(act_text)
exp_color="rgba(255, 250, 144, 1)"
exp_text="Dropped!"
assert act_text==exp_text,"Text is not matched"
print("Text is matched")
assert act_color==exp_color,"Color is not matched"
print("Color is matched")
#print(act_color)
driver.close()