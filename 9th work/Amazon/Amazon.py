from Baseclass.Chromepath.Pathfile import *
from selenium.webdriver.support.select import Select
driver.get("file:///C:/Users/admin/Desktop/multiselect.html")
driver.maximize_window()
lst=driver.find_element_by_xpath("//select[@id='multi']")
s=Select(lst)
for i in range(1,len(s.options)):
    if i%2==0:
       s.select_by_index(i)
       print([o.text for o in s.all_selected_options])










