#Handle multiple windows
from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\chromedriver.exe")
driver.get("https://www.flipkart.com")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//button[text()='✕']").click()
driver.find_element_by_xpath("//input[@name='q']").send_keys("iphone xr")
driver.find_element_by_xpath("//button[@type='submit']").click()
parentWindow=driver.current_window_handle
parent_title=driver.title
driver.find_element_by_xpath("//div[text()='Apple iPhone XR (White, 64 GB)']").click()
driver.find_element_by_xpath("//div[text()='Apple iPhone XR (White, 128 GB)']").click()
ExpTitle1="Apple iPhone XR ( 64 GB Storage, 0 GB RAM ) Online at Best Price On Flipkart.com"
ExpTitle2="Iphone Xr - Buy Products Online at Best Price in India - All Categories | Flipkart.com"
handle=driver.window_handles
for i in handle:
    driver.switch_to.window(i)
    if driver.title==ExpTitle1:
        driver.find_element_by_xpath("//button[text()='ADD TO CART']").click()
driver.switch_to.window(parentWindow)
driver.close()

