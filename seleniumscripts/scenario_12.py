from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
act=ActionChains(driver)
a=driver.find_element_by_xpath("//a[text()='Offers ']")
act.move_to_element(a).perform()
driver.find_element_by_xpath("//span[text()='20% off on making charge']").click()
act_msg=driver.find_element_by_xpath("//span[text()='20% off on making charge']").text
print(act_msg)
exp_msg='20% OFF ON MAKING CHARGE'
assert act_msg==exp_msg,print("fail")
print("pass")
