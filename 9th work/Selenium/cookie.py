from selenium import webdriver
driver=webdriver.Chrome('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\chromedriver.exe')
driver.get('http://localhost/login.do')
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_name('pwd').send_keys('manager')
driver.find_element_by_id('loginButtonContainer').click()
c1={'name' :'a','value':'apple','name':'b','value':'bat'}

driver.add_cookie(c1)
print(driver.get_cookie('b'))
driver.delete_all_cookies()
driver.close()