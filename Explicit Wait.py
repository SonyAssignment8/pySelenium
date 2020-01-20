from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('http://www.quora.com/Kevin-Rose')
element = WebDriverWait(driver,2).until(
    EC.presence_of_all_elements_located((by.PARTIAL_LINK-TEXT,"Followers"))

)
element.clcik()