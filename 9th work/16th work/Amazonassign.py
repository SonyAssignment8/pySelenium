#Goto Amazon select electronics options using visible text and print the result in the console
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\chromedriver.exe')
driver.get('https://www.amazon.in')
sel=driver.find_element_by_id("searchDropdownBox")
opt=Select(sel)
opt.select_by_visible_text("Electronics")
driver.find_element_by_xpath("//input[@type='submit']").click()
lst=driver.find_elements_by_xpath("//h4[text()='Electronics']/../../../ul")
for i in lst:
    print(i.text)