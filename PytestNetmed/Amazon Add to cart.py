from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(5)
driver.find_element_by_xpath(".//*[@id='usedBuySection']/i").click()
driver.find_element_by_xpath('//*[@id="a-autoid-1"]/span/input').click()

