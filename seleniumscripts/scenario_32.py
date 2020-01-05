from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_xpath("//li[@class='store-block']").click()
count=driver.find_elements_by_xpath("//ul[@class='side-bar']/li")
print(len(count))
for i in count:
    print(i.text)
