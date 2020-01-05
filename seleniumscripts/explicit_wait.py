from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
d=webdriver.Chrome()
d.get("https://www.quora.com/Kevin-Rose")
element=WebDriverWait(d,3).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,'Followers ')))
element.click()
