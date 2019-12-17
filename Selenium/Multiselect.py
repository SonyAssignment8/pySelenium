# Selecting all the even options from a multiselect option
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"C:\Users\Jyoti\AppData\Local\Programs\Python\Python35\Scripts\chromedriver.exe")
driver.get("file:///C:/Users/Jyoti/Desktop/cars.html")
driver.maximize_window()
lst_opts = driver.find_element_by_xpath("//select[@name='cars']")
sel = Select(lst_opts)
print(len(sel.options))
for i in range(0,len(sel.options)):
    if i % 2 == 0:
        sel.select_by_index(i)
        print([o.text for o in sel.all_selected_options])
