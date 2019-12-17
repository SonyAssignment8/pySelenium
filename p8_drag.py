from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(12)
driver.maximize_window()

driver.switch_to.frame(0)
source= driver.find_element_by_id("draggable")
dest= driver.find_element_by_id("droppable")
import time
time.sleep(10)
try:

    a = ActionChains(driver)
    #a.drag_and_drop(source,dest).perform()
    a.click_and_hold(source).move_to_element(dest).release().perform()

except:
    print("unable to drop")
finally:
    driver.close()