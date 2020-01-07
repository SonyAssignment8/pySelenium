'''Scenario 3
1. Open a browser of your choice say Mozilla Firefox
2. Navigate to http://jqueryui.com/droppable/ webpage.
3. Consider “Drag me to my target” as a source and “Drop here” as a target.
4. Write a code to perform drag and drop operation from source to target.
5. After drag and drop verify the operation is successfully by checking the color property of CSS and also verify text change.
 (Use assert statement to verify that color and text are as expected.)
 '''
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("http://jqueryui.com/droppable/")
driver.switch_to.frame(0)
dragelement=driver.find_element_by_xpath("//div[@id='draggable']")
dropelement=driver.find_element_by_xpath("//div[@id='droppable']")
ActionChains(driver).drag_and_drop(dragelement,dropelement).perform()
wb=driver.find_element_by_xpath("//div[@class='ui-widget-header ui-droppable ui-state-highlight']")
Acttext=wb.text
Exptext="Dropped!"
Expcolor="rgba(255, 250, 144, 1)"
Actcolor=wb.value_of_css_property("background-color")
assert Acttext==Exptext,"False"
print("The text is verified ---->Pass")
assert Actcolor==Expcolor,"False"
print("The background color is verified----->Pass")
driver.close()

