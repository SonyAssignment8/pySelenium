from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
act=ActionChains(driver)
w=driver.find_element_by_xpath("//a[contains(text(),'Coins ')]")
act.move_to_element(w).perform()
driver.find_element_by_xpath("//span[text()='Lakshmi Gold Coins']/../following-sibling::ul/li/span[text()='20 gram']").click()
act_url=driver.current_url
exp_ulr='https://www.bluestone.com/gold+coins/20-gram-24-kt-lakshmi-gold-coin~9164.html'
assert act_url==exp_ulr,print("fail")
print("pass")