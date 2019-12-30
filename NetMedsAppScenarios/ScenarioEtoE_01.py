from time import time

from selenium import webdriver
from NetMedsAppScenarios.Commondata import GetProperty
import time
import pytest

g = GetProperty()
u=g.getJsonProperty("config","url")
signinlinkxpath=g.getJsonProperty("login","signinlink")
uname=g.getJsonProperty("config","username")
pword=g.getJsonProperty("config","password")

usernameid=g.getJsonProperty("login","username")
buttonxpath=g.getJsonProperty("login","btn")
passwordid=g.getJsonProperty("login","password")
signinbtnxpath=g.getJsonProperty("login","signinbtn")

class NetMeds:

    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

    def launchbrowser(self):
        self.driver.implicitly_wait(20)
        self.driver.get(u)
        self.logintoAPP()

    def logintoAPP(self):
        self.driver.maximize_window()
        count=0
        while count<=60:
            try:
                self.driver.find_element_by_xpath(signinlinkxpath).click()
                break
            except Exception:
                count+=1
        self.driver.find_element_by_id(usernameid).send_keys(uname)
        time.sleep(2)
        self.driver.find_element_by_xpath(buttonxpath).click()
        self.driver.find_element_by_id(passwordid).send_keys(pword)
        self.driver.find_element_by_xpath(signinbtnxpath).click()
        self.fitnessProduct()
    def fitnessProduct(self):
        fitnesslinkxpath=g.getJsonProperty("home","fitness")
        catagoriesxpath=g.getJsonProperty("catogories","health_and_food")
        addtocartbtnxpath=g.getJsonProperty("cart","addtocart")
        cartbtn=g.getJsonProperty("cart","cartcount")
        cart_count=g.getJsonProperty("cart","countinsidecart")
        expected_result=g.getJsonProperty("result","expected")
        self.driver.find_element_by_xpath(fitnesslinkxpath).click()
        self.driver.find_element_by_xpath(catagoriesxpath).click()
        self.driver.execute_script("window.scrollBy(0,250)")
        self.driver.find_element_by_xpath(addtocartbtnxpath).click()
        self.driver.find_element_by_xpath(cartbtn).click()
        actual=self.driver.find_element_by_xpath(cart_count).text
        assert actual==expected_result;False
        print("1 item is present in cart")


    def logoutApp(self):
        logout_link_xpath=g.getJsonProperty("logout","logoutlink")
        logout_btn_xpath=g.getJsonProperty("logout","logoutbtn")
        self.driver.find_element_by_xpath(logout_link_xpath).click()
        self.driver.execute_script("window.scrollBy(0,500)")
        count = 0
        while count <= 60:
            try:
                self.driver.find_element_by_xpath(logout_btn_xpath).click()
                break
            except Exception:
                count += 1


n = NetMeds("chrome")
n.launchbrowser()
n.logoutApp()
