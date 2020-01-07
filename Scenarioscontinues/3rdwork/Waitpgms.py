#Explicit wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome("./chromedriver.exe")
# driver.get("https://www.quora.com/profile/Kevin-Rose")
# ELE=WebDriverWait(driver,2).until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Followers")))
# ELE.click()
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Python",Keys.ENTER)
