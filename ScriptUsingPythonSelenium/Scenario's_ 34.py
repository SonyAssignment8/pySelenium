'''
Scenario 34
1. open browser
2. enter url(yatra)
3. select boarding and de-boarding and select any cities
4. select any date and select return date and return date should be a difference of 15
days
5. Note: return date should be select dynamically it should not be hard-coded
6. select 2 adults 1 child and 1 infant
7. select premium economy
8. and capture no of flights available.
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import datetime

from selenium.webdriver.common.keys import Keys
from datetime import date


class Yatra:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

    def launchWebsite(self):
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.yatra.com/")
        time.sleep(3)
        self.boardingpoint()
    def boardingpoint(self):
        b_point=self.driver.find_element_by_id("BE_flight_origin_city")
        b_point.clear()
        time.sleep(3)
        b_point.send_keys("Bangalore",Keys.ENTER)
        d_point=self.driver.find_element_by_name("flight_destination")
        d_point.clear()
        time.sleep(5)
        d_point.send_keys("Maun")
        time.sleep(3)
        d_point.send_keys(Keys.ENTER)
        self.select_date()
    def select_date(self):
        self.driver.find_element_by_name("flight_origin_date").send_keys("January 20",Keys.ENTER)
        time.sleep(3)
        mon=str(date.today().month)
        ye=str(date.today().year)
        self.driver.find_element_by_id("20/0"+mon+"/2020").click()
        self.select_return_date()
    def select_return_date(self):
        time.sleep(5)
        self.driver.find_element_by_id("BE_flight_ret_cal").click()
        time.sleep(5)
        mon=str(date.today().month)
        self.driver.find_element_by_id("20/0"+mon+"/2020").click()
        self.select_passanger()

    def select_passanger(self):
        self.driver.find_element_by_id("BE_flight_paxInfoBox").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'Adult')]/../following-sibling::div/div/span[@class='ddSpinnerPlus']").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'Child')]/../following-sibling::div/div/span[@class='ddSpinnerPlus']").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'Infant')]/../following-sibling::div/div/span[@class='ddSpinnerPlus']").click()
        self.driver.find_element_by_id("BE_flight_flsearch_btn").click()
        self.driver.close()



b=Yatra("chrome")
b.launchWebsite()