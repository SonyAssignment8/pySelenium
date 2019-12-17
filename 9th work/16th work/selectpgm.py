from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\chromedriver.exe')
driver.implicitly_wait(3)
driver.get("https://Amazon.in")
sel=driver.find_element_by_id("searchDropdownBox")
a=Select(sel)
lst=a.options
for i in lst:
    print(i.text)

