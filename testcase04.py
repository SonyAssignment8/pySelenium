from selenium import webdriver
from selenium.webdriver.support.select import Select

browser=input("enter a browser:")
if browser=="Chrome":
    driver = webdriver.Chrome()
elif browser=="FireFox":
    driver=webdriver.Firefox()
else:
    driver=webdriver.Ie()

driver.get("https://in.ebay.com/")
driver.implicitly_wait(12)
driver.maximize_window()

def search():
    driver.find_element_by_id("gh-ac").send_keys("Apple watches")
    driver.find_element_by_id("gh-btn").click()
    return
search()

def category():
    s=driver.find_element_by_id("gh-cat")
    a = Select(s)

    a.select_by_visible_text("Smart Watches")
    driver.find_element_by_id("gh-btn").click()
    return
category()


# a method to print the result of the product.
def product():
    pro= driver.find_elements_by_xpath("//h3[@class='s-item__title']")
#printing all the values fron 1st page
    for i in pro:
        print(i.text)
    #6th select from list and print
    ele=pro[5]
    print("6th product is:",ele.text)
product()

