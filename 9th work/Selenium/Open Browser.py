from selenium import webdriver
# driver = webdriver.Chrome("C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\chromedriver.exe")f
driver = webdriver.Chrome()
driver.get("https://selenium.dev/")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//div[@class='download-button ide']").click()


