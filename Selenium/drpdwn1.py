from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"C:\Users\Jyoti\AppData\Local\Programs\Python\Python35\Scripts\chromedriver.exe")
driver.get("https://www.amazon.in/")
wb = driver.find_element_by_id('searchDropdownBox')
a = Select(wb)
a.select_by_visible_text("Electronics")
driver.find_element_by_xpath("//input[@class='nav-input']").click()
wb = driver.find_elements_by_xpath("//h4[text()='Electronics']/../../../ul")
for i in wb:
    print(i.text)
