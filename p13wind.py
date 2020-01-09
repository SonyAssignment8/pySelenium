from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element_by_name("field-keywords").send_keys("iphone xr")

driver.find_element_by_xpath("//input[@class='nav-input']").click()
p_wid=driver.window_handles[0]
time.sleep(5)
driver.find_element_by_xpath("//span[text()='Apple iPhone XR (64GB) - Yellow']").click()
time.sleep(5)
w=driver.window_handles[1]
time.sleep(5)
driver.switch_to.window(w)
a=driver.find_element_by_id("productTitle").text
print(a)
driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()

url= driver.title
print(url)
exp="Amazon.in Shopping Cart"
assert url == exp,False
True