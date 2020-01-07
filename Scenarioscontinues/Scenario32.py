'''Scenario 32
1. open browser
2. enter url(bluestone)
3. click on visit our stores
4. check the count of locations
5. close browser '''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.maximize_window()
#click on visit our stores icon
driver.find_element_by_xpath("//div[@class='prcs-d c-link']").click()
driver.execute_script("window.scrollBy(0,1000);")
place=driver.find_elements_by_xpath("//ul[@class='side-bar']/li")
#check the count of locations
print("Count of the location is:",len(place))
driver.close()