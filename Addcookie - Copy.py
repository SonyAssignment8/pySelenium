from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://www.linkedin.com/")
cookie = {'name':'atul', 'value':'values'}
driver.add_cookie(cookie)
driver.implicitly_wait(10)
print(driver.get_cookie("atul"))
driver.close()
# driver.delete_cookie()  # delete all cookies
