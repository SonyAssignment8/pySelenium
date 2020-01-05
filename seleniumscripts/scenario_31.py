from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_xpath("//a[text()='10+1 Monthly Plan']").click()
a=driver.find_element_by_id("amount")
a.send_keys("10000")
e=driver.find_element_by_id("Email")
e.send_keys("rashmi@gmail.com")
driver.find_element_by_id("gmsStart").click()
cur_url=driver.current_url
assert cur_url=="https://www.bluestone.com/goldmineOrder?execution=e5s1",print("fail")
print("pass")