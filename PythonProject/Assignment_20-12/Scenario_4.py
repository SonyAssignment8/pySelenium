import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver
def get_BrowserName(browser):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == 'firefox':
        return webdriver.Firefox()
    elif browser == 'safari':
        return webdriver.Safari()
    elif browser == 'ie':
        return webdriver.InternetExplorer()
    else:
        return webdriver.Chrome()

def homePage():
    driver.find_element_by_xpath("//input[@label='Search for anything']").send_keys("Apple Watches")
    sel = driver.find_element_by_xpath("//select[@aria-label='Select a category for search']")
    options = Select(sel)
    options.select_by_visible_text("Jewelry & Watches")
    driver.find_element_by_xpath("//input[@value='Search']").click()


def product_result():
    res = driver.find_elements_by_xpath("//h1/span")
    for i in res:
        print(i.text,end =" ")
        print()

def product_list_frstPage():
    prdct_lst = driver.find_elements_by_xpath("//li[@class='s-item   ']//h3")
    time.sleep(2)
    for i in prdct_lst:
        print(i.text)

def search_product():
    prdct_to_srch = "Apple Watch Nike Plus series 2 42mm stainless steel band"
    prdct_lst = driver.find_elements_by_xpath("//li[@class='s-item   ']//h3")
    time.sleep(2)
    for i in prdct_lst:
        if prdct_to_srch == i.text:
            print(i.text)
            break

browser = input("Enter the browser name:")
driver = get_BrowserName(browser)
driver.get("https://in.ebay.com/")
homePage()
print("============================================================")
product_result()
print("============================================================")
product_list_frstPage()
print("============================================================")
search_product()
