from selenium import webdriver

# webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
from selenium.webdriver.common.keys import Keys
user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://www.linkedin.com/")
element = driver.find_element_by_id("email","password")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()