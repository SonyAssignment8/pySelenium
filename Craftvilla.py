from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://www.craftsvilla.com/")
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='KURTIS & DRESSES ']").click()
driver.find_element_by_xpath("//span[text()='2000-5000']").click()
driver.find_element_by_xpath("//input[@id='price_2000-5000']").click()