from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("mobiles")
driver.find_element_by_xpath("//input[@value='Go']").click()
import time
time.sleep(5)
driver.find_element_by_xpath("//span[text()='Redmi 7A (Matte Blue, 2GB RAM, 16GB Storage)']").click()
driver.find_element_by_xpath("//span[text()='Samsung Galaxy M30s (Sapphire Blue, 4GB RAM, Super AMOLED Display, 64GB Storage, 6000mAH Battery)']").click()
pwindow=driver.current_window_handle
windows=driver.window_handles
exp_text="Xiaomi Mi A3 (More Than White, 6GB RAM, AMOLED Display, 128GB Storage, 4030mAH Battery): Amazon.in: Electronics"
for i in windows:
    driver.switch_to_window(i)
    actul_text=driver.title
    if actul_text.__contains__(exp_text):
        driver.find_element_by_xpath("//a[text()='Redmi Note 8 Pro (Halo White, 6GB RAM, 64GB Storage)']").click()


