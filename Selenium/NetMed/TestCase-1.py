# Global driver object
import time

from selenium import webdriver
from NetMed.BaseClass import getJsonProperty


class NetMeds:
    # Launch the browser
    def get_BrowserName(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'safari':
            self.driver = webdriver.Safari()
        elif browser == 'ie':
            self.driver = webdriver.InternetExplorer()
        else:
            self.driver = webdriver.Chrome()

    # Login to application
    def loginToApp(self):

        url = getJsonProperty("config", "URL")
        self.driver.maximize_window()
        self.driver.get(url)

        # FRAME = getJsonProperty("signin", "frm")
        # self.driver.switch_to_frame(FRAME)
        #
        # notify_clk = getJsonProperty("signin", "notification")
        # self.driver.find_element_by_xpath(notify_clk).click()
        #
        # sign_in_lnk = getJsonProperty("signin", "signin_lnk")
        # count = 0
        # while count <= 10:
        #     try:
        #         self.driver.find_element_by_xpath(sign_in_lnk).click()
        #         break
        #     except:
        #         print("Exception handled")
        #         count += 1
    def sel_product(self):
        FITNESS = getJsonProperty("prodct_tab","fitness")
        self.driver.find_element_by_xpath(FITNESS).click()

        categry = getJsonProperty("prodct_tab","category")
        self.driver.find_element_by_xpath(categry).click()

        time.sleep(4)
        brnd = getJsonProperty("prodct_tab","brand")
        self.driver.find_element_by_xpath(brnd).click()


obj = NetMeds()
brwr = getJsonProperty("config", "browser")
obj.get_BrowserName(brwr)
obj.loginToApp()
obj.sel_product()
