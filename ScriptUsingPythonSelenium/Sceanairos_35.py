'''
Scenario 35 1. open browser
 2. enter url(https://jqueryui.com/slider/)
 3. Slide the slider upto end in multiples times  it should come in reverse order in multiple times.
4. close Browser.
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/")
driver.find_element_by_link_text("Slider").click()
driver.switch_to.frame(0)
wb1=driver.find_element_by_xpath("//div[@id='slider']")
act=ActionChains(driver)
act.drag_and_drop_by_offset(wb1,275,0).perform()
act.drag_and_drop_by_offset(wb1,0,0).perform()
act.drag_and_drop_by_offset(wb1,-100,0).perform()
act.drag_and_drop_by_offset(wb1,-175,0).perform()
act.drag_and_drop_by_offset(wb1,-225,0).perform()
#close the browser
driver.close()