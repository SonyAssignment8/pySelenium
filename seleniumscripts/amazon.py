from selenium import  webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://www.amazon.in/")
sel=Select(driver.find_element_by_id("searchDropdownBox"))
sel.select_by_visible_text("Electronics")
driver.find_element_by_class_name("nav-input").click()
list=driver.find_element_by_xpath("//div[@class='a-row a-expander-container a-expander-extend-container']")
print(list.text)
