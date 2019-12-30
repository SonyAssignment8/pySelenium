#use of window handles
from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\chromedriver.exe")
driver.get("https://www.flipkart.com")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//button[text()='✕']").click()
driver.find_element_by_xpath("//input[@name='q']").send_keys("iphone xr")
driver.find_element_by_xpath("//button[@type='submit']").click()
parentWindow=driver.window_handles[0]
driver.find_element_by_xpath("//div[text()='Apple iPhone XR (White, 64 GB)']").click()
childWindow=driver.window_handles[1]
driver.switch_to.window(childWindow)
driver.find_element_by_xpath("//button[@type='button']").click()
driver.switch_to.window(parentWindow)
driver.find_element_by_xpath("//input[@name='q']").clear()
driver.quit()