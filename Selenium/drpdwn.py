from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sel = driver.find_element_by_id("searchDropdownBox")
a = Select(sel)
a.select_by_visible_text("Books")
print(a.__getattribute__())
a.select_by_index(5)
a.select_by_value("search-alias=apparel")
driver.close()
