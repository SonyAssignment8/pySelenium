import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path="C:\\Users\\Jyoti\\PycharmProjects\\Selenium\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.craftsvilla.com/")
driver.implicitly_wait(20)
driver.find_element_by_xpath("//a[text()='KURTIS & DRESSES ']").click()
time.sleep(4)
driver.find_element_by_xpath("//label[@title='2000-5000']").click()
time.sleep(4)
price_lst = driver.find_elements_by_xpath("//p/span[@class='product-offer-price']")
for i in price_lst:
    a = i.text
    if 2000 <= int(a[2::]) <= 5000:
        print(a[2::])
