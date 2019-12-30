from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(r"D:\Python\chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(12)
driver.maximize_window()
driver.switch_to.frame(0)
drag = driver.find_element_by_id("draggable")

drop = driver.find_element_by_id("droppable")
try:
    actions = ActionChains(driver)
   # actions.drag_and_drop(drag,drop).perform()
    actions.click_and_hold(drag).move_to_element(drop).release().perform()

except:
    print("error")
finally:
    driver.close()