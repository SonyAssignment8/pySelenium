'''Scenario 34
1. open browser
2. enter url(yatra)
3. select boarding and de-boarding and select any cities
4. select any date and select return date and return date should be a difference of 15 days
5. Note: return date should be select dynamically it should not be hard-coded
6. select 2 adults 1 child and 1 infant
7. select premium economy
8. and capture no of  flights available.
 '''

import time
from selenium import webdriver
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.yatra.com/")
time.sleep(5)
#enter depart place
driver.find_element_by_xpath("//input[@id='BE_flight_origin_city']").click()
time.sleep(2)
driver.find_element_by_xpath("//p[@class='ac_cityname' and contains(text(),'Hyderabad ')]").click()
time.sleep(2)

#enter destination place
driver.find_element_by_xpath("//input[@id='BE_flight_arrival_city']").click()
driver.find_element_by_xpath("//p[@class='ac_cityname' and contains(text(),'Bangalore ')]").click()

#select the depart date
driver.find_element_by_xpath("//label[@for='BE_flight_origin_date']").click()
time.sleep(2)
date='10/01/2020'
driver.find_element_by_xpath("//td[@data-date='10/01/2020']").click()
depart=int(date[0:2:])
arr=depart+15
#Select the arrival date
driver.find_element_by_xpath("//input[@id='BE_flight_arrival_date']").click()
driver.find_element_by_xpath("//td[@data-date='+arr+']").click()


#select 2 adults 1 child and 1 infant
driver.find_element_by_xpath("//i[@class='icon icon-angle-right arrowpassengerBox pax-active']").click()
driver.find_element_by_xpath("//div[@data-flightagegroup='adult' and @class='adultcount']//span[@class='ddSpinnerPlus']")









