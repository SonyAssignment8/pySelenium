from selenium import webdriver
import time
driver=webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.implicitly_wait(20)
driver.get("https://www.amazon.in/")
dp=driver.find_element_by_id("searchDropdownBox")
sel=Select(dp)
lst=sel.options
for i in lst:
    print(i.text)

