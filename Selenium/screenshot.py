from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.jobsforher.com/")
driver.save_screenshot("my.png")
sleep(4)
driver.close()