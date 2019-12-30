from ScriptUsingPythonSelenium.BaseClass import*
driver.get("https://www.amazon.in/")
dd=driver.find_element_by_id("searchDropdownBox")
dd.click()
