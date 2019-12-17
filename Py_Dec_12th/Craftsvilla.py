from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.craftsvilla.com/")
#driver.implicitly_wait(30)
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='KURTIS & DRESSES ']").click()
driver.find_element_by_xpath("//label[@for='price_2000-5000']").click()
list_of_price = driver.find_elements_by_xpath("//span[@class='product-offer-price']")
x =0
#time.sleep(10)
for i in list_of_price:
    t = i.text
    print(t)
    x = int(t[2:])
assert x>=2000 and x<=5000,"False"
print("True")
driver.close()
