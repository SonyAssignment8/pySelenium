#Use javascript to click on a particular element
from selenium import webdriver
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.Vtiger.com")
privacy=driver.