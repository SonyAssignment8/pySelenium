from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(12)
driver.maximize_window()
select = driver.find_element_by_id("searchDropdownBox")
a = Select(select)
print(a.select_by_visible_text("Books").text)
a.select_by_index(3)
a.select_by_value("search-alias=automotive")
driver.close()