import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.find_element_by_id('twotabsearchtextbox').send_keys("mobiles")
driver.find_element_by_xpath("//input[@class='nav-input']").click()
time.sleep(2)
driver.find_element_by_xpath("//span[text()='Redmi 7A (Matte Blue, 2GB RAM, 16GB Storage)']").click()
time.sleep(2)
driver.find_element_by_xpath("//span[text()='Redmi 7A (Matte Gold, 2GB RAM, 16GB Storage)']").click()
# driver.find_element_by_xpath("//span[text()='Honor 9N (Blue, 4GB RAM, 64GB Storage)']").click()
parent_win = driver.current_window_handle
windws = driver.window_handles
match_txt = "Redmi 7A (Matte Gold, 2GB RAM, 16GB Storage): Amazon.in: Electronics"
for i in windws:
    driver.switch_to.window(i)
    act_txt = driver.title
    if act_txt == match_txt:
        driver.find_element_by_xpath("//input[@name='submit.add-to-cart']").click()
        print("Product added to cart")
driver.switch_to.window(parent_win)
driver.close()