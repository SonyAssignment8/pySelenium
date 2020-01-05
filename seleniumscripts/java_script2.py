import time
from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.get("https://www.bluestone.com")
polices=d.find_element(By.XPATH,"//span[text()='POLICIES']")
d.execute_script("arguments[0].scrollIntoView();",polices)
time.sleep(3)
