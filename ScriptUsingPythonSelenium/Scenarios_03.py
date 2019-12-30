from selenium import webdriver
#launch browser
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(20)
#enter the URL
driver.get("https://jqueryui.com")

driver.find_element_by_xpath("//a[text()='Droppable']").click()
driver.switch_to.frame(0)
drag_element=driver.find_element_by_id("draggable")
drop_element=driver.find_element_by_id("droppable")
ActionChains(driver).drag_and_drop(drag_element,drop_element).perform()
expected_text="Dropped!"
actual_text=drop_element.text
assert actual_text==expected_text;False
print("Text is verified successfully...")
expected_color="rgba(119, 118, 32, 1)"
actual_color=drop_element.value_of_css_property("color")
assert actual_color==expected_color;False
print("colour is verified successfully.....")
driver.close()