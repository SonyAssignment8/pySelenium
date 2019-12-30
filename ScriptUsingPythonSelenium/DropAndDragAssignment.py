from selenium import webdriver
import time
driver=webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.implicitly_wait(20)
driver.get("https://www.amazon.in/")
dp=driver.find_element_by_id("searchDropdownBox")
sel=Select(dp)
sel.select_by_visible_text("Electronics")
time.sleep(2)
driver.find_element_by_xpath("//input[@type='submit']").click()
lst=driver.find_elements_by_xpath("//h4[text()='Electronics']/../../../ul")
for i in lst:
    print(i.text)

driver.close()