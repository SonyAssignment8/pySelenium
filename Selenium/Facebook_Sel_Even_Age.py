from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"C:\Users\Jyoti\AppData\Local\Programs\Python\Python35\Scripts\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//a[text()='Create New Account']").click()
age_lst = driver.find_elements_by_id('year')
age_options =age_lst.find_elements_by_tag_name("option")
for option in age_options:
    print("Value is: %s" % age_options.get_attribute("value"))
    age_options.click()
# evenLst= list(filter(lambda age_lst: age_lst.text % 2 == 0, age_lst))
# print(evenLst)