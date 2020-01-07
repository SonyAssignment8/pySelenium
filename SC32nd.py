from builtins import print

from selenium import webdriver
import time
#1 Open browser
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#2 Enter URL(bluestone)
driver.get("https://www.bluestone.com/")
driver.maximize_window()
driver.implicitly_wait(12)

#3click on visit our stores
driver.find_element_by_xpath("//span[contains(text(),'Locate')]").click()
lst_of_stores = []
#4 check the count of locations
wb_store = driver.find_elements_by_xpath("//ul[@class='side-bar']")
print("Count of the cities",wb_store.__sizeof__())
for i in wb_store:
    i.text
driver.close()


