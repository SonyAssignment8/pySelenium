from selenium import webdriver
from selenium.webdriver.support.select import Select

#driver=webdriver.Chrome(executable_path="C:\\Users\\ankita\\PycharmProjects\\pgm\\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(12)
driver.maximize_window()
select = driver.find_element_by_id("searchDropdownBox")
#print(select.text)
a= Select(select)

a.select_by_visible_text("Amazon Fashion")
a.select_by_index(1)
a.select_by_value("search-alias=alexa-skills")


driver.close()