from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
wb = driver.find_element_by_id('searchDropdownBox').click()
sel = Select(wb)
for i in iter(sel):
    sel.select_by_visible_text().text