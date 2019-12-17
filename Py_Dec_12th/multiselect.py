#selecting all the even options from a multiselect options
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Akshay/Desktop/multiselect.html")
driver.maximize_window()
lst_options = driver.find_element_by_xpath("//select[@name='cars']")
sel = Select(lst_options)
print(len(sel.options))
for i in range(1,len(sel.options)):
    if i%2==0:
        sel.select_by_index(i)
        print([o.text for o in sel.all_selected_options])
