'''Scenario 35
1. open browser
2. enter url(https://jqueryui.com/slider/)
3. Slide the slider upto end in multiples times  it should come in reverse order in multiple times.
4. close Browser
 '''
#open the browser
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to the jquerty page
slide=driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
time.sleep(4)
#Switch to frame
driver.switch_to_frame(0)
ele=driver.find_element_by_xpath("//div[@id='slider']")
act=ActionChains(driver)
act.drag_and_drop_by_offset(ele,0,200).perform()
act.drag_and_drop_by_offset(ele,200,300).perform()
act.drag_and_drop_by_offset(ele,300,-200)



