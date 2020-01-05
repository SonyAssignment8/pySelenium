from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.quora.com/Kevin-Rose")
element = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Followers")))
element.click()
