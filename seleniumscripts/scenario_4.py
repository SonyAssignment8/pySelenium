from selenium import webdriver
import time
#driver=webdriver.Chrome()
from selenium.webdriver.support.select import Select
browser=input("enter the browser name:")
if browser=="Chrome":
    driver=webdriver.Chrome()
elif browser=="Firefox":
    driver=webdriver.Firefox()
driver.get("https://in.ebay.com/")

def search(data):
    driver.find_element_by_id("gh-ac").send_keys(data)
    driver.find_element_by_id("gh-btn").click()

def category(option):
    w=driver.find_element_by_id("gh-cat")
    sel=Select(w)
    sel.select_by_visible_text(option)
    driver.find_element_by_id("gh-btn").click()
def capture_data():
   lst=driver.find_elements_by_xpath("//a[@class='s-item__link']")
   for i in lst:
       print(i.text)

search(" Apple Watches")
time.sleep(3)
category("Jewelry & Watches")
time.sleep(2)
capture_data()