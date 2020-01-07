'''Scenario 26
1. Open browser
2. enter URL(bluestone)
3. scroll upto some axis
4. check whether top icon  is displayed or not
5. if it displayed click on it
6. close browser Scenario '''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,2000);")
driver.save_screenshot("top.png")
