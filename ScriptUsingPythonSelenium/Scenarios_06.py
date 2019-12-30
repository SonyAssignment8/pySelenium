'''Scenario 6
1. Open Browser
2. Pass URL (Bluestone)
3. Move Cursor to Rings Menu
4. Select Diamond Rings and click on it
5. Get Prise list By default
6. Select sort by and Select price low to high
7. Get Prise list price low to high
8. Compare By default price and Sorted price
9. and Verify sorted price should in ascending order.
10. Close Browser'''
from selenium import webdriver
from selenium.webdriver import ActionChains


class BlueStone:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

    def launchWebsite(self):
        self.driver.get("https://www.bluestone.com/")
        self.ringslink()

    def ringslink(self):
        custom_drop = self.driver.find_element_by_xpath("//a[text()='Rings ']")
        act = ActionChains(self.driver)
        act.move_to_element(custom_drop).perform()
        self.driver.find_element_by_xpath("//a[text()='Diamond']").click()

    def default_price(self):
        def_price_list = self.driver.find_elements_by_xpath("//span[@class='new-price']")
        price = []
        for i in def_price_list:
            price.append(i.text.replace("RS", "").replace(".", "").replace(",", ""))
        return price

    def low_to_high_price(self):
        sort_menu = self.driver.find_element_by_xpath("//span[@class='view-by-wrap title style-outline i-right']")
        act = ActionChains(self.driver)
        act.move_to_element(sort_menu).perform()
        self.driver.find_element_by_xpath("//a[text()='Price Low to High ']").click()
        sorted_price_list = self.driver.find_elements_by_xpath("//span[@class='new-price']")
        price = []
        for i in sorted_price_list:
            price.append(i.text.replace("RS", "").replace(".", "").replace(",", ""))
        return price

    def isAscending(self, l):
        previous = l[0]
        for number in l:
            if number < previous:
                return False
            previous = number
        return True
    # print("sorted price in ascending order==>",self.low_to_high_price())


b = BlueStone("chrome")
b.launchWebsite()
b.default_price()
lst = b.low_to_high_price()
flag = b.isAscending(lst)
if flag == True:
    print("price list is sorted.....")
else:
    print("price list is not sorted")

