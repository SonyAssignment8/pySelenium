from selenium import webdriver
from selenium.webdriver.support.select import Select

#driver=webdriver.Chrome(executable_path="C:\\Users\\ankita\\PycharmProjects\\pgm\\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(12)
driver.maximize_window()
select = driver.find_element_by_id("searchDropdownBox")
a= Select(select)
#print(select.text)

a.select_by_visible_text("Electronics")
driver.find_element_by_xpath("//input[@class='nav-input']").click()
list1=driver.find_element_by_xpath("//div[@class='a-row a-expander-container a-expander-extend-container']")
print(list1.text)
