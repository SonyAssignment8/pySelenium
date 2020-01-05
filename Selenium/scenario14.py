from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("https://www.bluestone.com/")
driver.maximize_window()
mousehover=driver.find_element_by_xpath("//a[text()='Coins ']")
a=ActionChains(driver)
a.move_to_element(mousehover).perform()
time.sleep(3)
driver.find_element_by_xpath("//span[text()='1 gram']").click()

driver.close()