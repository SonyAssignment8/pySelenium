from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Chrome(r"D:\Python\chromedriver.exe")
driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
driver.implicitly_wait(12)
driver.switch_to.frame(0)
slide = driver.find_element_by_xpath("//div[@id='slider']/span")
try:
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slide,100,0).perform()
    time.sleep(3)
except:
    print("Error")
finally:
    driver.close()