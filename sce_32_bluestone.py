'''
Scenario 32
1. open browser
 2. enter url(bluestone)
  3. click on visit our stores
   4. check the count of locations
   5. close browser
'''
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_xpath("//div[@class='prcs-d c-link']").click()
list_stores=driver.find_elements_by_xpath("//ul[@class='side-bar']")
for i in list_stores:
    print(i.text)
driver.close()
