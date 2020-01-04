from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
driver.find_element_by_id("BE_flight_origin_city").click()
import time
time.sleep(2)
driver.find_element_by_xpath("//p[@class='ac_cityname' and contains(text(),'Bangalore')]").click()
time.sleep(2)
driver.find_element_by_xpath("//p[@class='ac_cityname' and contains(text(),'Mumbai')]").click()
time.sleep(2)
driver.find_element_by_xpath("//li[@class='datepicker flex1']").click()
time.sleep(2)
driver.find_element_by_xpath("//td[@id='04/01/2020']").click()
time.sleep(2)
def returndate(date):
    driver.find_element_by_xpath("//li[@class='datepicker flex1']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//td[@id='"+date+"']").click()

returndate("10/01/2020")
time.sleep(2)
driver.find_element_by_xpath("//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']").click()
driver.find_element_by_xpath("//div[@data-flightagegroup='adult' and @class='pax-limit clearfix col-x-fluid']//span[@class='ddSpinnerPlus']").click()
driver.find_element_by_xpath("//div[@data-flightagegroup='child' and @class='pax-limit clearfix col-x-fluid']//span[@class='ddSpinnerPlus']").click()
driver.find_element_by_xpath("//div[@data-flightagegroup='infant' and contains(@class,'pax-limit clearfix col-x-fluid')]//span[@class='ddSpinnerPlus']").click()
driver.find_element_by_xpath("//span[text()='Premium Economy']").click()
driver.find_element_by_id("BE_flight_flsearch_btn").click()
list_flights=driver.find_elements_by_xpath("//span[@class='i-b text ellipsis']")
for i in list_flights:
    lst=i.text
    print(lst)
#driver.find_element_by_xpath("//p[contains(text(),'DEL')]").click()
#driver.find_element_by_xpath("//a[contains(text(),'Multi-City')]").click()
# driver.find_element_by_xpath("//a[contains(text(),'Add City')]").click()

# act=ActionChains(driver)
# act.click_and_hold(wb1).perform()
driver.close()