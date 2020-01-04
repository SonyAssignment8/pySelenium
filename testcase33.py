from selenium.webdriver import ActionChains
import time
from selenium import webdriver

class Bluestones:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

    def launchWebsite(self):
        self.driver.get("https://www.bluestone.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return

    def search(self):
        self.driver.find_element_by_name("search_query").send_keys("Rings")
        self.driver.find_element_by_name("submit_search").click()
        self.driver.window_handles[0]
        self.driver.find_element_by_xpath("//img[@alt='The Maidel Ring']").click()
        w=self.driver.window_handles[1]
        self.driver.switch_to.window(w)
        actual_price=self.driver.find_element_by_xpath("//span[@id='our_price_display']").text
        print("Actual price:",actual_price)
        dis_price=self.driver.find_element_by_xpath("//span[@id='discountedPriceSpan']").text
        print("Discount price :",dis_price)
        i=str(actual_price)
        i1=str(dis_price)
        actual_price=i.replace(",","")
        dis_price=i1.replace(",","")
        i2=int(actual_price)
        i3=int(dis_price)
        print("Difference",i2-i3)
        assert actual_price==dis_price, False
        True

        self.driver.close()


b=Bluestones('chrome')
b.launchWebsite()
b.search()

