'''Scenario 4
1. Open any Browser of your choice (Mozilla firefox, Chrome, Internet Explorer or Safari).
Write the code in such way that based on argument passed respective browser is selected.
2. Browse to Ebay website.
3. Write a method which do following:
4. On the homepage, there is a search box, type some product (say Apple Watches).
5. From categories dropdown, select the category of your product (say Watches).
6. Click Search button.
7. Write a method to print the result of the product.
8. Write a method to print Nth product say 10th Product.
9. Write a method to print all products from 1st page.
10. Write a method to print all products along with scroll down. '''
import time
from webbrowser import browser
from selenium.webdriver.support.select import Select
from selenium import webdriver

def browser_launch(browser):
    if browser=="Chrome":
       return webdriver.Chrome("./chromedriver.exe")
    elif browser=="Firefox":
       return webdriver.Firefox()
    elif browser=="InternetExplorer":
       return webdriver.InternetExplorer()
    elif browser=="Safari":
       return webdriver.safari()
    else:
        return webdriver.Chrome()
driver=browser_launch("Chrome")
driver.get("https://in.ebay.com/")
def home():
    select=driver.find_element_by_name("_sacat")
    move=Select(select)
    move.select_by_visible_text("Jewelry & Watches")
    time.sleep(4)
    driver.find_element_by_xpath("//input[@type='text']").send_keys("Apple Watches")
    driver.find_element_by_xpath("//input[@id='gh-btn']").click()
def display_result():
    result=driver.find_element_by_xpath("//div[@class='srp-controls__control srp-controls__count']//h1//span[1]")
    print("Number of results is:",result.text)
def search_product():
    lst_result=driver.find_elements_by_xpath("//a//h3")
    for i in lst_result:
        actual=i.text
        n="Canary 44mm Apple Watch Series 4 Custom Bezel Band Bracelet Baguette Diamond"
        if actual==n:
            print(actual)
def print_products():
    lst_result = driver.find_elements_by_xpath("//a//h3")
    for i in lst_result:
        print(i.text)


home()
display_result()
search_product()
print_products()


