from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(3)
driver.find_element_by_id("twotabsearchtextbox").send_keys("Camera, Canon EOS 700D")
driver.find_element_by_xpath("//input[@class='nav-input']").click()
driver.find_element_by_xpath(
    "//span[text()='Canon EOS 1500D 24.1MP Digital SLR Camera (Black) with 18-55 and 55-250mm is II Lens, 16GB Card and Carry Case']").click()
child=driver.window_handles[1]
driver.switch_to.window(child)
driver.find_element_by_xpath("//span[@id='acrCustomerReviewText']").click()