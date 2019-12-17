from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(15)
#click on menu
select = driver.find_element_by_id("searchDropdownBox")
a = Select(select)
#select by electonics
a.select_by_visible_text("Electronics")
driver.find_element_by_xpath("//input[@class='nav-input']").click()
#print side menu bar details
sideBar= driver.find_element_by_xpath("//div[@class='a-row a-expander-container a-expander-extend-container']")
print(sideBar.text)
for i in sideBar:
    print(i.text)
print(select.text)
for i in select.text:
    print(i,end="")