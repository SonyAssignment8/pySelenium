from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("file:///C:/Users/rashmi/Desktop/web.html")
sel=Select(driver.find_element_by_class_name("custom-select"))
l=len(sel.options)
print(l)
print(sel.is_multiple)
for i in range(0,l):
    if i%2==0:
        sel.select_by_index(i)
for j in sel.all_selected_options:
    print(j.text)


