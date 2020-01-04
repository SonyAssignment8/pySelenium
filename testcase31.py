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
        self.driver.find_element_by_xpath("//a[text()='10+1 Monthly Plan']").click()
        self.driver.find_element_by_name("amount").send_keys("5000")
        self.driver.find_element_by_id("Email").send_keys("afu@gmail.com")
        self.driver.find_element_by_id("gmsStart").click()
        time.sleep(1)

        self.driver.find_element_by_id("fullname").send_keys("sariya")

        self.driver.find_element_by_id("contactNumber").send_keys("9874896321")

        self.driver.find_element_by_id("address").send_keys("Mumbai")

        self.driver.find_element_by_id("postcode_delivery").send_keys("590037")
        self.driver.find_element_by_name("_eventId_savePersonalAddressDetails").click()

        self.driver.find_element_by_id("nomineeName").send_keys("xiz")
        self.driver.find_element_by_name("_eventId_checkoutSaveAddressDetails").click()
        act_page_url = self.driver.current_url
        # print(act_page_url)
        expe_page_url = "https://www.bluestone.com/goldmineOrder?execution=e1s3"
        assert act_page_url == expe_page_url, "Test Case Fail"
        print("Payment page must be displayed")

        # act=self.driver.current_url
        # print(act)
        # exp="https://www.bluestone.com/goldmineOrder?execution=e1s1"
        # assert act==exp,False
        # True


b=Bluestones('chrome')
b.launchWebsite()
b.search()

