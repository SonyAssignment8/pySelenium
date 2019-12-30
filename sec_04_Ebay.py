'''
1. Open any Browser of your choice (Mozilla firefox, Chrome, Internet Explorer or Safari). Write the code in such way
that based on argument passed respective browser is selected.
 2. Browse to Ebay website.
  3. Write a method which do following:
   4. On the homepage, there is a search box, type some product (say Apple Watches).
    5. From categories dropdown, select the category of your product (say Watches).
    6. Click Search button.
     7. Write a method to print the result of the product.
     8. Write a method to print Nth product say 10th Product.
9. Write a method to print all products from 1st page.
 10. Write a method to print all products along with scroll down.

'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
def select_browser(browser):
    if browser=="chrome":
        return webdriver.Chrome()
    elif browser=="firefox":
        return webdriver.Firefox()
def search_product(name):
    driver.find_element_by_id("gh-ac").send_keys(name)
    sel=driver.find_element_by_xpath("//select[@class='gh-sb gh-sprRetina']")
    sel.click()
    sel_item=Select(sel)
    sel_item.select_by_visible_text("Jewelry & Watches")
    driver.find_element_by_id("gh-btn").click()
def products_Count():
    count_list=driver.find_element_by_xpath("//h1[@class='srp-controls__count-heading']").text
    print("Total no of products in a list----",count_list)
def print_product():
    list_item = driver.find_elements_by_xpath("//h3[@class='s-item__title s-item__title--has-tags']")
    for i in list_item:
        exp_txt=i.text
        act_text="Sport Apple Watch Band Series 1 2 3 4 Apple Watch 38mm/42mm"
        if exp_txt==act_text:
            print(exp_txt)

def products_list():
    list_item = driver.find_elements_by_xpath("//h3[@class='s-item__title s-item__title--has-tags']")
    for i in list_item:
        print(i.text)
def printall_products():
     intsize=driver.find_elements_by_xpath("//iframe")
     length=len(intsize)
     print(length)
     import time
     time.sleep(6)
     driver.switch_to.frame("master-1")
     list_01=driver.find_element_by_xpath("//a[contains(text(),'Lavish Yet Affordable - Beautiful Gold ')]").click()

driver=select_browser("chrome")
driver.maximize_window()
driver.get("https://in.ebay.com/")
search_product("Apple watch")
print("============================")
products_list()
print("============================")
products_Count()
print("============================")
print_product()
print("==============================")
printall_products()
driver.close()
