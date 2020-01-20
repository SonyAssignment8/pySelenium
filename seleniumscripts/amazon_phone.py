from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone xr")
driver.find_element_by_class_name("nav-input").click()
driver.find_element_by_xpath("//span[text()='Apple iPhone XR (64GB) - Yellow']").click()
w=driver.window_handles
i=iter(w)
pid=next(i)
cid=next(i)
driver.switch_to_window(cid)
driver.find_element_by_id("submit.add-to-cart").click()

