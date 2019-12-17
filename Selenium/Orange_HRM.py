
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Jyoti\AppData\Local\Programs\Python\Python35\Scripts\chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()
driver.find_element_by_id('welcome').click()
driver.find_element_by_link_text('Logout').click()
print("Success")