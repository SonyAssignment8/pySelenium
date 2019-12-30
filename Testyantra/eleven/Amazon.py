from selenium.webdriver.support.select import Select
driver = webdriver.Chrome
select =Select("searchDropdownDescription")
select.select_by_index()
select.select_by_value()
select.deselect_by_visible_text()