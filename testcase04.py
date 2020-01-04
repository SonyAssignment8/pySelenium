from selenium import webdriver
from selenium.webdriver.support.select import Select

class BlueStone:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

    def launchWebsite(self):
        self.driver.get("https://in.ebay.com/")
        self.driver.implicitly_wait(12)
        self.driver.maximize_window()



    def search(self):
        self.driver.find_element_by_id("gh-ac").send_keys("Apple watches")
        self.driver.find_element_by_id("gh-btn").click()
        return


    def category(self):
        s=self.driver.find_element_by_id("gh-cat")
        a = Select(s)

        a.select_by_visible_text("Smart Watches")
        self.driver.find_element_by_id("gh-btn").click()
        return

    def product(self):
        pro = self.driver.find_elements_by_xpath("//h3[@class='s-item__title']")
        # printing all the values fron 1st page
        for i in pro:
            print(i.text)
        # 6th select from list and print
        ele = pro[5]
        print("6th product is:", ele.text)

# a method to print the result of the product.

b=BlueStone('chrome')
b.launchWebsite()
b.search()
b.category()
b.product()

