'''Scenario 4
1. Open any Browser of your choice (Mozilla firefox, Chrome, Internet Explorer or
Safari). Write the code in such way that based on argument passed respective browser is
selected.
2. Browse to Ebay website.
3. Write a method which do following:
4. On the homepage, there is a search box, type some product (say Apple Watches).
5. From categories dropdown, select the category of your product (say Watches).
6. Click Search button.
7. Write a method to print the result of the product.
8. Write a method to print Nth product say 10th Product.
9. Write a method to print all products from 1st page.
10. Write a method to print all products along with scroll down.'''
from selenium import webdriver
from selenium.webdriver.support.select import Select


class Ebay:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

    def launchWebsite(self):
        self.driver.get("https://www.ebay.com")
        self.searchProduct()

    # search product
    def searchProduct(self):
        self.driver.find_element_by_xpath("//input[@label='Search for anything']").send_keys("Apple Watches")
        # sel_element=self.driver.find_element_by_id("gh-cat")
        # Select(sel_element).select_by_visible_text("All Categories")
        self.driver.find_element_by_id("gh-btn").click()

    # Products available
    def listOfProduct(self):
        product_list = self.driver.find_elements_by_xpath("//a[@class='s-item__link']")
        total_count = 0
        for i in product_list:
            total_count += 1
            print(i.text)

        print("total count of product in a page is:==>", total_count)
        count = 0
        for i in product_list:

            count += 1
            if count == 10:
                print("==================")
                return i.text

    def print_10th_product(self):

        print("10th product in the list is:=", self.listOfProduct())
        self.driver.close()


e = Ebay("chrome")
e.launchWebsite()
e.print_10th_product()
