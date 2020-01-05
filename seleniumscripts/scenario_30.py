from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_xpath("//a[text()='10+1 Monthly Plan']").click()
driver.find_element_by_id("gmsStart").click()
a=driver.find_element_by_xpath("//ul[@id='amount_error']").text
b=driver.find_element_by_xpath("//ul[@id='Email_error']").text
print(a,b)
act_msg="Amount is required"
assert a==act_msg and b=="Email is required",print("fail")
print("pass")

